<script>
	import Loader from "./Loader.svelte";

	export let collection;


	function getThumbnail(uri) {
		const indexId = uri.endsWith("/manifest") ? uri.replace('https://lbiiif.riksarkivet.se/arkis!', '').replace('/manifest', '') : uri.replace('https://lbiiif.riksarkivet.se/', '');

		console.log(window.imageIndex[indexId] ? window.imageIndex[indexId] : false)
		return window.imageIndex[indexId] ? window.imageIndex[indexId] : false;
	}

	let subCollections;
	let hasLoaded;;
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
					thumbnail: getThumbnail(item.id),
				}
			});
			hasLoaded = true;
		});
</script>

<div>
	{#if subCollections && subCollections.length > 0}
	<div class="columns responsive-container">
		{#each subCollections as item}
			{#if item.type === "Collection"}
				<a href="?collection={item.id}">
					{#if item.thumbnail}
						<img aria-hidden="true" src="https://lbiiif.riksarkivet.se/arkis!{item.thumbnail}/square/350,/0/default.jpg">
					{/if}
					{item.label}
				</a>
			{:else if item.type === "Manifest"}
				<a href="?manifest={item.id}">
					{#if item.thumbnail}
						<img aria-hidden="true" src="https://lbiiif.riksarkivet.se/arkis!{item.thumbnail}/square/350,/0/default.jpg">
					{/if}
					{item.label}
				</a>
			{/if}
		{/each}
	</div>
	{:else if hasLoaded}
		<p>Inga publika arkiv.</p>
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
		border-bottom: 8px solid #e8a621;
		margin: 0rem .5rem .5rem 0rem;
		float: left;
	}
	
	a:hover, a:focus, a:active {
		background: #f4ca47;
		border-bottom: 8px solid #f4ca47;
	}

	img {
		width: 100%;
	}
</style>