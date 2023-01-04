# Grid Browser

Svelte application for browsing media from IIIF collections and manifests.

## Development setup

Install the dependencies...

```bash
cd grid-browser
npm install
```

...then start [Rollup](https://rollupjs.org):

```bash
npm run dev
```

Navigate to [localhost:8080](http://localhost:8080). You should see the app running.

By default, the server will only respond to requests from localhost. To allow connections from other computers, edit the `sirv` commands in package.json to include the option `--host 0.0.0.0`.

## Building and running in production mode

To create an optimized version of the app:

```bash
npm run build
```

You can run the newly built app with `npm run start`. This uses [sirv](https://github.com/lukeed/sirv), which is included in your package.json's `dependencies` so that the app will work when you deploy to PaaS services.


## Single-page app mode

By default, sirv will only respond to requests that match files in `public`. This is to maximise compatibility with static fileservers, allowing you to deploy your app anywhere.

If you're building a single-page app (SPA) with multiple routes, sirv needs to be able to respond to requests for *any* path. You can make it so by editing the `"start"` command in package.json:

```js
"start": "sirv public --single"
```

## URL usage

The application can be used with the following URL parameters. If none are given the application will enter "browsing" mode and show the root collection.

 - `manifest` - URL to an IIIF manifest or collection to show in "dark table" mode. Note that you can stack URIs by comma separation to combine multiple manifests/collections.
 - `date=true` - Show date slider in "dark table" mode. This parameter will filter out all items which can't be dated, you might end up with an empty page if not careful.
 - `collection` - URL to an IIIF collection to start from in "browsing" mode.

## Configure curated collections

When both in "browsing" mode and without the `collection` parameter set, the application will show a curated list of collections.

These can be configured in [`App.svelte`](https://github.com/Abbe98/ra-sokprototyper/blob/3fd67754a14044ec34ccf244a72ed0e8197309b5/grid-browser/src/App.svelte#L192-L195). Each entry is a `<Block>` component with the following properties, the last one being optional:

```html
<Block
  title="Marinens ritningar"
  thumbnail="https://lbiiif.riksarkivet.se/arkis!K0035322_00001/square/350,/0/default.jpg"
  manifest="https://lbiiif.riksarkivet.se/collection/arkiv/lAELykjdz1EZN9cxABCer7"
  timeline="true"
/>
```
