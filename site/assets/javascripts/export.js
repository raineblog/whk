const exportParam = new URLSearchParams(location.search).get('export')?.toLowerCase();
if (exportParam === 'true') {
    document$.subscribe(({ body }) => {
        console.log("export");
    });
}
else {
    console.log("attempt to load giscus");
    load_giscus();
    document$.subscribe(({ body }) => {
        console.log("not export");
    });
}
