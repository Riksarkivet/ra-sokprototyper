<script>
	import Loader from "./Loader.svelte";

	export let collection;

	let subCollections;
	fetch(collection)
		.then((response) => {
			return response.json();
		})
		.then((data) => {
			subCollections = data.items.map(item => {
				if (item.type === "Canvas") return;
				return {
					id: item.id,
					label: item.label.sv[0],
					type: item.type,
				}
			});
		});
</script>

<div>
	{#if subCollections && subCollections.length > 0}
		{#each subCollections as item}
			{#if item.type === "Collection"}
				<a href="?collection={item.id}">
					{item.label}
				</a>
			{:else if item.type === "Manifest"}
				<a href="?manifest={item.id}">
					{item.label}
				</a>
			{/if}
		{/each}
	{:else}
		<Loader />
	{/if}
</div>

<style>
	a {
		width: 200px;
		display: block;
		background: #e8a621;
		color: black;
		text-decoration: none;
		text-align: center;
		line-height: 1.7;
		padding: 8px 0px;
		margin: 0rem .5rem .5rem 0rem;
		float: left;
	}
	
	a:hover, a:focus, a:active {
		background: #f4ca47;
	}
</style>