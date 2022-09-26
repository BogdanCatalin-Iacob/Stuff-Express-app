// scroll to top variables
let arrowUp = document.getElementById('btn-up');

// sorting variables
let sort;
let direction;
let selector = document.getElementById('sort-selector');
let currentUrl = new URL(window.location);

/**Split the values of selected option for sorting products,
 * set the values to the window
 * and reload the page
 */
function sortParameters() {
    let selectedValue = selector.value;
    if (selectedValue != 'reset') {
        let option = selectedValue.split('_');
        if (option.length > 2) {
            sort = option[0] + '_' + option[1];
            direction = option[2];
        } else {
            sort = option[0];
            direction = option[1];
        }

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
}

/**
 * Scroll the page back to top
 * when the displayed button is clicked
 */
function scrollToTop(){
    window.scrollTo(0,0);
}

selector.addEventListener("change", sortParameters);
arrowUp.addEventListener("click", scrollToTop);