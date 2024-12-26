
window.onload = function () {
	const inputs = document.querySelectorAll('.form-control input');

	inputs.forEach(input => {
		input.addEventListener('focus', function() {
			this.previousElementSibling.style.display = 'none';
		});

		input.addEventListener('blur', function() {
			if (this.value === '') {
				this.previousElementSibling.style.display = 'block';
			}
		});
	});

	const labels = document.querySelectorAll(".form-control label");
	labels.forEach(label => {
		label.innerHTML = label.innerText.split('').map((letter, index) => `<span style="transition-delay:${index * 35}ms">${letter}</span>`).join('');
	});
};
