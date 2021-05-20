<template>
	<div
		class="graphical-input"
		ref="graphicalInput"
		:style="inputStyle"
		@click="onClick"
	></div>
</template>

<script>
export default {
	props: {
		modelValue: Object,
		passimage: String,
		inputs: {
			type: Number,
			default: 5
		}
	},
	computed: {
		inputStyle () {
			return {
				backgroundImage: `url('https://picsum.photos/500/500')` ,
				width: `${this.gridSize}px`,
				height: `${this.gridSize}px`
			}
		}
	},
	mounted () {
		const windowWidth = window.outerWidth
		if (windowWidth < 350) {
			this.gridSize = 250
		}
		else if (windowWidth < 480) {
			this.gridSize = 350
		}
		else if (windowWidth < 550) {
			this.gridSize = 450
		}
		else {
			this.gridSize = 500
		}
	},
	data () {
		return {
			inputData: [],
			inputsCount: 0,
			circleDiameter: 40,
			gridSize: null,
			animationDuration: 200
		}
	},
	methods: {
		onClick ($event) {
			this.inputsCount += 1
			const { offsetX, offsetY } = $event
			const coordinates = {
				x: offsetX,
				y: offsetY
			}
			this.inputData.push(coordinates)
			this.createClickElementEffect(coordinates)
			if (this.inputsCount === this.inputs) {
				this.updateValue()
				this.resetData()
			}
		},
		createClickElementEffect (coordinates) {
			const circleElement = document.createElement('DIV')
			circleElement.classList.add('graphical-input__circle')
			circleElement.style.left = `${coordinates.x - this.circleDiameter / 2}px`
			circleElement.style.top = `${coordinates.y - this.circleDiameter / 2}px`
			circleElement.style.width = `${this.circleDiameter}px`
			circleElement.style.height = `${this.circleDiameter}px`
			circleElement.style.animationDuration = `${this.animationDuration}ms`
			
			this.$refs.graphicalInput.appendChild(circleElement)
			setTimeout(() => {
				this.$refs.graphicalInput.removeChild(circleElement)
			}, this.animationDuration + 100)
		},
		updateValue () {
			this.$emit('update:modelValue', {
				inputs: this.inputData,
				gridSize: this.gridSize
			})
		},
		resetData () {
			this.inputsCount = 0
			this.inputData = []
		}
	}
}
</script>

<style lang="scss">
@keyframes pulse {
	0% {
		transform: scale(0.7);
		opacity: 0;
	}
	30% {
		opacity: 1;
	}
	100%{
		transform: scale(1);
		opacity: 0;
	}
}
.graphical-input {
	cursor: pointer;
	position: relative;
	overflow: hidden;
	border-radius: 3px;
	border: solid 1px $color-gray !important;

	&__circle {
		position: absolute;
		opacity: 0;
		background-color: rgba($color-blue, .6);
		border-radius: 50%;
		animation-name: pulse;
		animation-timing-function: ease-in-out;
	}
}
</style>