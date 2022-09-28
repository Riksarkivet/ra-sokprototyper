<script>
    import { createEventDispatcher } from 'svelte';
    export let decade = 1750;
    export let canNavigateBack;
    export let canNavigateForward;

    const dispatch = createEventDispatcher();
    function previousDecade() { dispatch('navigation', { 'action': 'previous' })};
    function nextDecade() { dispatch('navigation', { 'action': 'next' })};
</script>

<nav>
    <div>
        {#if canNavigateBack}<button on:click="{previousDecade}">&#9664;</button>{/if}<span>{ decade }</span>{#if canNavigateForward}<button on:click="{nextDecade}">&#9654;</button>{/if}
    </div>
</nav>

<style>
nav {
	display: flex;
	justify-content: center;
	padding-bottom: 1em;
	font-size: larger;
}

div {
	display: flex;
	align-items: center;
	justify-content: center;
}

button {
	border: none;
	margin: 0;
	padding: 0;
	background: none;
	color: var(--ra-font-color);
	font-size: larger;
	cursor: pointer;
	line-height: normal;
	transform: scale(0.7);
}

button:hover, button:focus {
	transform: scale(0.8);
}

span {
	font-size: 140%;
	margin: 0 3px;
}
</style>