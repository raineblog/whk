import yargs from 'yargs';
import { hideBin } from 'yargs/helpers';
import gulp from 'gulp';
import sourcemaps from 'gulp-sourcemaps';
import posthtml from 'gulp-posthtml';
import htmlmin from 'gulp-htmlmin';
import postcss from 'gulp-postcss';
import terser from 'gulp-terser';
import path from 'path';

// import plumber from 'gulp-plumber';

// PostHTML Plugins
import posthtmlPostcss from 'posthtml-postcss';
import posthtmlAltAlways from 'posthtml-alt-always';
import posthtmlLinkPreload from 'posthtml-plugin-link-preload';
import { posthtmlExternalLink } from 'posthtml-external-link';
import posthtmlRemoveDuplicates from 'posthtml-remove-duplicates';
import mergeInlineLonghand from 'posthtml-postcss-merge-longhand';

// PostCSS Plugins
import autoprefixer from 'autoprefixer';
import postcssNested from 'postcss-nested';
import cssnano from 'cssnano';
// import combineSelectors from 'postcss-combine-duplicated-selectors';
// import atImport from 'postcss-import';

const posthtmlImgAlt = () => (tree) => {
  tree.walk((node) => {
    if (node.tag === 'img' && node.attrs && node.attrs.src) {
      if (!node.attrs.alt || node.attrs.alt.trim() === '') {
        const src = node.attrs.src;
        // Use path.posix.basename to handle forward slashes in URLs correctly
        const fileName = path.posix.basename(src, path.posix.extname(src));
        node.attrs.alt = decodeURIComponent(fileName) || 'image';
      }
    }
    return node;
  });
};

const argv = yargs(hideBin(process.argv)).argv;
const inputDir = argv.inputDir || 'dist';
const outputDir = argv.outputDir || 'dest';

const postcss_plugins = [
  postcssNested(),
  autoprefixer(),
  cssnano(),
  // combineSelectors({ removeDuplicatedProperties: true }),
  // atImport()
];

const posthtml_plugins = [
  posthtmlPostcss(postcss_plugins),
  posthtmlImgAlt(),
  posthtmlAltAlways(),
  mergeInlineLonghand(),
  posthtmlLinkPreload(),
  posthtmlExternalLink(),
  posthtmlRemoveDuplicates('meta')
];

const htmlmin_options = {
  collapseWhitespace: true,
  removeComments: true,
  removeEmptyAttributes: true,
  minifyJS: true,
  minifyCSS: true,
  useShortDoctype: true
};

function processHtml() {
  return gulp.src(
    `${inputDir}/**/*.html`,
    { dot: true }
  )
    // .pipe(plumber())
    .pipe(posthtml(posthtml_plugins))
    .pipe(htmlmin(htmlmin_options))
    .pipe(gulp.dest(outputDir));
}

function processJs() {
  return gulp.src(
    `${inputDir}/**/*.js`,
    { dot: true }
  )
    // .pipe(plumber())
    .pipe(sourcemaps.init())
    .pipe(terser({
      keep_classnames: true,
      keep_fnames: true
    }))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(outputDir));
}

function copyAssets() {
  return gulp.src([
    `${inputDir}/**/*`,
    `!${inputDir}/**/*.html`,
    `!${inputDir}/**/*.css`,
    `!${inputDir}/**/*.js`
  ], {
    dot: true,
    encoding: false
  }).pipe(gulp.dest(outputDir));
}

function processCss() {
  return gulp.src(`${inputDir}/**/*.css`, { dot: true })
    // .pipe(plumber())
    .pipe(sourcemaps.init())
    .pipe(postcss(postcss_plugins))
    .pipe(sourcemaps.write('.'))
    .pipe(gulp.dest(outputDir));
}

export default gulp.series(processHtml, processJs, copyAssets, processCss);