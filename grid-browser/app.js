function loadFromManifest(data) {
    let title;
    let source;
    let date;
    data.metadata.forEach(item => {
        if (item.label.sv[0] == 'Titel') {
            title = item.value.none[0];
        } else if (item.label.sv[0] == 'Källhänvisning') {
            source = item.value.none[0];
        } else if (item.label.sv[0] == 'Datering') {
            date = item.value.none[0];
        }
    });

    data.items.forEach(item => {
        if (item.type == 'Canvas') {
            let image = item.id.replace('/canvas', '/square/200,/0/default.jpg');
            let link = item.id.replace('/canvas', '').replace('https://lbiiif.riksarkivet.se/arkis!', 'https://sok.riksarkivet.se/bildvisning/');
            let html = '<div class="image"><a href="' + link + '"><img src="' + image + '"></a></div>';
            html += '<div class="title">' + title + '</div>';
            html += '<div class="source">' + source + '</div>';
            html += '<div class="date">' + date + '</div>';
            document.querySelector('#images').innerHTML = document.querySelector('#images').innerHTML + html;
        }
    });
}

let foundURIs = [];
let title;
function traverse(url) {
  fetch(url).then(response => {
    return response.json()
  }).then(data => {
    if (!foundURIs.length) {
        title = data.label.sv[0];
        document.title = title;
    }

    if (data.type == 'Manifest') {
        loadFromManifest(data);
    }

    foundURIs.push(url);

    for(let item of data.items) {
        if (!foundURIs.includes(item.id)) {
            if (item.type == 'Manifest') {
                traverse(item.id);
            } else if (item.type == 'Collection') {
                traverse(item.id);
            }
        }
    }
  });
}

// get get parameter "manifest"
let manifest = new URLSearchParams(window.location.search).get('manifest');

traverse(manifest);
