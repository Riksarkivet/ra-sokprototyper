<div class="spinner"></div>

<style>
    .spinner {
        display: block;
        width: 80px;
        height: 80px;
        margin: auto;
    }
    .spinner:after {
        content: " ";
        display: block;
        width: 64px;
        height: 64px;
        margin: 8px;
        border-radius: 50%;
        border: 6px solid var(--ra-blue-main);
        border-color: var(--ra-blue-main) transparent var(--ra-blue-main) transparent;
        animation: spinner 1.2s linear infinite;
    }
    @keyframes spinner {
        0% {
            transform: rotate(0deg);
        }
        100% {
            transform: rotate(360deg);
        }
    }
</style>