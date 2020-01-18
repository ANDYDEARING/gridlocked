const currentPage = document.querySelector('#body').dataset.currentpage;
document.querySelector('#'+currentPage+'-link').classList.add("active", "disabled");