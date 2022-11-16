<script>
    import { createEventDispatcher, onMount, onDestroy } from 'svelte';
    export let isModalOpen;
    export let currentCanvas;
    let infoURL;
    let sourceURL;

    const dispatch = createEventDispatcher();
    function close() { dispatch('modal-close')};

    if (isModalOpen) {
        infoURL = 'https://lbiiif.riksarkivet.se/' + currentCanvas.split('/')[3] + '/info.json';
        sourceURL = currentCanvas.replace("/square/350,/0/default.jpg", "").replace("https://lbiiif.riksarkivet.se/arkis!", "https://sok.riksarkivet.se/bildvisning/");
    }

    let map;
    onMount(async () => {
        console.log('onMount');
        map = window.L.map('modal', {
            center: [0, 0],
            zoom: 1,
            attributionControl: false,
            zoomControl: false,
            crs: window.L.CRS.Simple,
        });
        window.L.tileLayer.iiif(infoURL).addTo(map);

        const closeButton = window.L.Control.extend({
            options: {
                position: 'topright'
            },
            onAdd: function (map) {
                const container = window.L.DomUtil.create('div', 'leaflet-bar leaflet-control leaflet-control-custom');
                container.innerHTML = '<a href="#" role="button" title="Stäng"><svg aria-hidden="true" style="transform: scale(1.7); height: 30px;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16"><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg></a>';
                container.addEventListener('click', close);
                return container;
            }
        });

        const infoButton = window.L.Control.extend({
            options: {
                position: 'topright'
            },
            onAdd: function (map) {
                const container = window.L.DomUtil.create('div', 'leaflet-bar leaflet-control leaflet-control-custom');
                container.innerHTML = '<a href="' + sourceURL + '" target="_blank" title="Navigera till källa"><svg xmlns="http://www.w3.org/2000/svg" aria-hidden="true" style="transform: scale(1.7); height: 30px;" width="16" height="16" fill="currentColor" class="bi bi-info" viewBox="0 0 16 16"><path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533L8.93 6.588zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/></svg></a>';
                return container;
            }
        });

        new closeButton().addTo(map);

        window.L.control.zoom({
            position: 'topright'
        }).addTo(map);

        new infoButton().addTo(map);
    });

    onDestroy(() => {
        map.remove();
        map = null;
    });

    function handleKeydown(event) {
        if (event.key === 'Escape') {
            close();
        }
    }
</script>

<div id="background" on:click={close}></div>
<div id="modal"></div>
<svelte:window on:keydown={handleKeydown}/>

<style>
#background {
    display: block;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.4);
}

#modal {
    display: block;
    position: fixed;
    z-index: 2;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background: #0b151f;
    width: 90%;
    height: 90%;
}
</style>
