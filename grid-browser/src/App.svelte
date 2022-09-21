<script>
	import Loader from "./Loader.svelte";

	let items = [];
	function loadFromManifest(data) {
		let title;
		let source;
		let date;
		data.metadata.forEach((item) => {
			if (item.label.sv[0] == "Titel") {
				title = item.value.none[0];
			} else if (item.label.sv[0] == "Källhänvisning") {
				source = item.value.none[0];
			} else if (item.label.sv[0] == "Datering") {
				date = item.value.none[0];
			}
		});

		data.items.forEach((item) => {
			if (item.type == "Canvas") {
				let image = item.id.replace(
					"/canvas",
					"/square/350,/0/default.jpg"
				);
				let link = item.id
					.replace("/canvas", "")
					.replace(
						"https://lbiiif.riksarkivet.se/arkis!",
						"https://sok.riksarkivet.se/bildvisning/"
					);
				items.push({
					title: title,
					source: source,
					date: date,
					image: image,
					link: link,
				});
				items = items; // for the Svelte compiler https://svelte.dev/tutorial/updating-arrays-and-objects
			}
		});
	}

	let foundURIs = [];
	let title;
	function traverse(url) {
		fetch(url)
			.then((response) => {
				return response.json();
			})
			.then((data) => {
				if (!foundURIs.length) {
					title = data.label.sv[0];
					document.title = title;
				}

				if (data.type == "Manifest") {
					loadFromManifest(data);
				}

				foundURIs.push(url);

				for (let item of data.items) {
					if (!foundURIs.includes(item.id)) {
						if (item.type == "Manifest") {
							traverse(item.id);
						} else if (item.type == "Collection") {
							traverse(item.id);
						}
					}
				}
			});
	}

	let manifest = new URLSearchParams(window.location.search).get("manifest");
	traverse(manifest);
</script>

<main>
	<h1>{title}!</h1>
	{#if items.length > 0}
		<div class="container">
			{#each items as item}
				<a href={item.link}>
					<img src={item.image} alt="{item.title}" />
				</a>
			{/each}
		</div>
	{:else}
		<Loader />
	{/if}
</main>

<style>
.container {
	display: grid;
	grid-template-columns: repeat(8, 1fr);
}

.container a {
	overflow: hidden;
	aspect-ratio: 1;
}

.container a > img {
	width: 100%;
}
</style>
