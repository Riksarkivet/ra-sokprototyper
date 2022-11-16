<script>
    import { createEventDispatcher, onMount, onDestroy } from 'svelte';
    export let isModalOpen;
    export let currentCanvas;
    let infoURL;

    const dispatch = createEventDispatcher();
    function close() { dispatch('modal-close')};

    if (isModalOpen) {
        infoURL = 'https://lbiiif.riksarkivet.se/' + currentCanvas.split('/')[3] + '/info.json';
    }

    let map;
    onMount(async () => {
        console.log('onMount');
        map = window.L.map('modal', {
            center: [0, 0],
            attributionControl: false,
            zoom: 0,
            crs: window.L.CRS.Simple,
        });
        window.L.tileLayer.iiif(infoURL).addTo(map);
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
