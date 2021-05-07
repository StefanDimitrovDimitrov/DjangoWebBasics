function Collapse(event) {
    console.log('works')
    // event.target.style.display = 'none'
}


function initExpand() {

    const items = [...document.getElementsByClassName('collapse-toggle')];
    items.forEach(item => {
        item.addEventListener('click', Collapse)
    })
}
