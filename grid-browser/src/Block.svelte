<script>
	export let title;
	export let thumbnail;
	export let manifest;
</script>

<a class="btn btn-block" href="?manifest={manifest}">
	<img aria-hidden="true" src="{thumbnail}">
	<span>{title}</span>
</a>

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
	margin: .5em;
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