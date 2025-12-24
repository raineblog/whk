function do_export() {
    document$.subscribe(({ body }) => {
        console.log("export");
    });
}

const exportParam = new URLSearchParams(location.search).get('export')?.toLowerCase();

if (exportParam === 'true') {
    do_export();
}
else {
    load_giscus();

    document$.subscribe(({ body }) => {
        console.log("not export");
    });
}
