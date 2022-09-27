<script>
    import { createEventDispatcher } from 'svelte';
    export let decade = 1750;

    const dispatch = createEventDispatcher();
    function previousDecade() { dispatch('navigation', { 'action': 'previous' })};
    function nextDecade() { dispatch('navigation', { 'action': 'next' })};
</script>

<nav>
    <div>
        <button on:click="{previousDecade}">&lt;</button> {decade} <button on:click="{nextDecade}">&gt;</button>
    </div>
</nav>

<style>
nav {
	display: flex;
	justify-content: center;
	padding-bottom: 1em;
	font-size: larger;
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
}
</style>