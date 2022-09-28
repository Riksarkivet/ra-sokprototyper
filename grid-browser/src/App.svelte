<script>
	import DateFilter from "./DateFilter.svelte";
	import Loader from "./Loader.svelte";
	import { beforeUpdate } from 'svelte';

	let allItems = [];
	let activeItems = [];
	function loadFromManifest(data) {
		let title;
		let source;
		let date;
		let decade;
		data.metadata.forEach((item) => {
			if (item.label.sv[0] == "Titel") {
				title = item.value.none[0];
			} else if (item.label.sv[0] == "Källhänvisning") {
				source = item.value.none[0];
			} else if (item.label.sv[0] == "Datering") {
				date = item.value.none[0];

				// we allways try to get the decade as to avoid computing it on the fly during filtering
				if (date.length == 4 && !isNaN(date)) { // parseInt is too forgiving on its own
					decade = Math.floor(parseInt(date)/10)*10;
				} else {
					decade = null;
				}
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
					allItems.push({
					title: title,
					source: source,
					date: date,
					image: image,
					link: link,
					decade: decade,
				});
				allItems = allItems; // for the Svelte compiler https://svelte.dev/tutorial/updating-arrays-and-objects
				activeItems = allItems; // we set all items as active to trigger beforeUpdate which will preform filtering
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
			})
	}
	let manifest = new URLSearchParams(window.location.search).get("manifest");
	
	if (manifest) {
		traverse(manifest);
	} else {
		title = 'Riksarkivet';
	}


	let inputManifest;
	function loadFromManifestInput() {
		traverse(inputManifest);
		window.history.pushState(
			{},
			"",
			`?manifest=${inputManifest}`
		);
	}
	


	let date = new URLSearchParams(window.location.search).get("date");

	let activeDecade = 0;
	let decades;
	let previousDecade;
	let nextDecade;
	beforeUpdate(() => {
		if (date) {
			// we use the median existing decade as a starting point
			decades = [...new Set(allItems.map(item => item.decade))].sort();
			const medianDecade = decades[Math.floor(decades.length / 2)];
			if (!userHasInteracted) activeDecade = medianDecade;

			filterDate();
		} else {
			activeItems = allItems;
		}
	});

	function filterDate() {
		activeItems = allItems.filter(item => item.decade === activeDecade);
		previousDecade = decades[decades.indexOf(activeDecade) - 1];
		nextDecade = decades[decades.indexOf(activeDecade) + 1];
	}

	let userHasInteracted = false;
	function dateFilterChanged(event) {
		const navigation = event.detail.action;
		userHasInteracted = true;
		if (navigation == 'previous') {
			activeDecade = previousDecade;
		} else {
			activeDecade = nextDecade;
		}
		filterDate();
	}
</script>

<main>
	<nav>
		<h1>{title}</h1>
		{#if date}
			<DateFilter decade={activeDecade} canNavigateBack={previousDecade} canNavigateForward={nextDecade} on:navigation="{dateFilterChanged}"/>
		{/if}
	</nav>
	{#if activeItems.length > 0 }
		<div class="container">
			{#each activeItems as item}
				<a href={item.link} target="_blank">
					<img src={item.image} alt="{item.title}" />
				</a>
			{/each}
		</div>
	{:else if manifest}
		<Loader />
	{:else}
	<form on:submit|preventDefault="{loadFromManifestInput}">
		<label for="iiif-input">IIIF Manifest</label>
		<input id="iiif-input" type="url" placeholder="https://lbiiif.riksarkivet.se/collection/arkiv/8XCsKmH8XKATnPaXVPaWf2" bind:value="{inputManifest}" />
		<button type="submit">Ladda</button>
	</form>
	{/if}
</main>

<style>
nav {
	padding: 0 10px;
	border-bottom: 6px solid var(--ra-blue-main);
}

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
