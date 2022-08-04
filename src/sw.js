/**
 * service worker 安装激活
 */

let dataCacheName = "cache-data-v1";
let cacheName = "eoelol-cache-1";
let filesToCache = [
    "./",
    "./index.html",
    "./src/main.css",
    "./assets/font/霞鹭尚智黑.woff2",
    "./assets/images/icons/128.png",
    "./assets/images/icons/144.png",
    "./assets/images/icons/192.png",
    "./assets/images/icons/256.png",
    "./assets/images/icons/512.png",
];

self.addEventListener("install", function (e) {
    console.log("SW Installed.");
    e.waitUntil(
        caches.open(cacheName).then(function (cache) {
            console.log("SW precaching.");
            return cache.addAll(filesToCache);
        })
    );
    self.skipWaiting();
});

self.addEventListener("activate", function (e) {
    console.log("SW Activate.");
    e.waitUntil(
        caches.keys().then(function (keyList) {
            return Promise.all(
                keyList.map(function (key) {
                    if (key !== cacheName && key !== dataCacheName) {
                        console.log("SW Removing old cache", key);
                        return caches.delete(key);
                    }
                })
            );
        })
    );
    return self.clients.claim();
});

self.addEventListener("fetch", function (e) {
    console.log("SW Fetch", e.request.url);
    // 如果数据相关的请求，需要请求更新缓存
    let dataUrl = "/mockData/";
    if (e.request.url.indexOf(dataUrl) > -1) {
        e.respondWith(
            caches.open(dataCacheName).then(function (cache) {
                return fetch(e.request)
                    .then(function (response) {
                        cache.put(e.request.url, response.clone());
                        return response;
                    })
                    .catch(function () {
                        return caches.match(e.request);
                    });
            })
        );
    } else {
        e.respondWith(
            caches.match(e.request).then(function (response) {
                return response || fetch(e.request);
            })
        );
    }
});
