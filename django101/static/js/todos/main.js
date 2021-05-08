function Collapse(event) {
    console.log('works')
    // event.target.style.display = 'none'
}

window.onload= function(){

    const items = [...document.getElementsByClassName('collapse-toggle')];
    items.forEach(item => {
        item.addEventListener('click', Collapse)
    }

)}
