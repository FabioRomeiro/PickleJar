<template>
	<div class="graphical-input">

		<div class="graphical-input__steps" v-if="withSteps">
			<div
				class="graphical-input__step"
				:class="{'graphical-input__step--active': step <= inputsCount}"
				v-for="step in inputs"
				:key="step"
			>
				{{ step }}
			</div>
		</div>

		<div
			class="graphical-input__input"
			ref="graphicalInput"
			:style="inputStyle"
			@click="onClick"
		></div>
	</div>
</template>

<script>
export default {
	props: {
		modelValue: Object,
		passimage: String,
		withSteps: Boolean,
		inputs: {
			type: Number,
			default: 5
		}
	},
	computed: {
		inputStyle () {
			return {
				backgroundImage: `url(${this.passimage})`,
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
				if (this.$refs.graphicalInput) {
					this.$refs.graphicalInput.removeChild(circleElement)
				}
			}, this.animationDuration + 100)
		},
		updateValue () {
			const data = {
				inputs: this.inputData,
				gridSize: this.gridSize
			}
			this.$emit('update:modelValue', data)
			this.$emit('update', data)
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

	display: flex;
	align-items: center;
	flex-direction: column;

	&__steps {
		width: 100%;
		display: flex;
		justify-content: space-between;
		align-items: center;
		margin-bottom: spacing(3);
	}

	&__step {
		width: 40px;
		height: 40px;
		border-radius: 40px;
		background-color: $color-gray-light;
		display: flex;
		align-items: center;
		justify-content: center;
		text-align: center;
		font-size: 20px;
		font-weight: 500;
		border: solid 1px $color-gray;
		color: $color-gray-dark;
		transition: border-color .3s ease-in-out, color .3s ease-in-out, background-color .3s ease-in-out;

		&--active {
			background-color: $color-green-extra-light;
			color: $color-green-dark;
			border-color: $color-green-dark;
		}
	}

	&__input {
		cursor: pointer;
		position: relative;
		overflow: hidden;
		border-radius: 3px;
		border: solid 1px $color-gray !important;
		background-position: center;
		background-size: cover;
	}

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