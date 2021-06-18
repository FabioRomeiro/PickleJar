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

		<CustomButton class="graphical-input__show-input-button" @click="toggleShowSequence">
			{{ showSequence ? 'Esconder' : 'Mostrar' }} sequência
		</CustomButton>

		<div
			class="graphical-input__input"
			:class="{'graphical-input__input--show-sequence': showSequence}"
			ref="graphicalInput"
			:style="inputStyle"
			@click="onClick"
		>
			<div
				ref="sequenceGrid"
				class="graphical-input__sequence_grid"
				v-show="showSequence"
			></div>
		</div>
	</div>
</template>

<script>
import CustomButton from '@/components/Forms/CustomButton'

export default {
	props: {
		modelValue: Object,
		passimage: String,
		withSteps: Boolean,
		clearResults: {type: Boolean, default: true},
		inputs: {
			type: Number,
			default: 5
		}
	},
	components: {
		CustomButton
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
			animationDuration: 200,
			showSequence: false
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
				if (this.clearResults) {
					this.resetData()
				}
			}
		},
		createCircleElement (coordinates, withAnimation, sequenceNumber) {
			const circleElement = document.createElement('DIV')
			circleElement.classList.add('graphical-input__circle')
			circleElement.style.left = `${coordinates.x - this.circleDiameter / 2}px`
			circleElement.style.top = `${coordinates.y - this.circleDiameter / 2}px`
			circleElement.style.width = `${this.circleDiameter}px`
			circleElement.style.height = `${this.circleDiameter}px`
			if (withAnimation) {
				circleElement.style.animationDuration = `${this.animationDuration}ms`
				circleElement.classList.add('graphical-input__circle--animated')
			}
			if (sequenceNumber) {
				circleElement.innerText = sequenceNumber
			}
			return circleElement
		},
		createClickElementEffect (coordinates) {
			const circleElementAnimated = this.createCircleElement(coordinates, true)
			this.$refs.graphicalInput.appendChild(circleElementAnimated)
			setTimeout(() => {
				if (this.$refs.graphicalInput) {
					this.$refs.graphicalInput.removeChild(circleElementAnimated)
				}
			}, this.animationDuration + 100)

			const circleElement = this.createCircleElement(coordinates, false, this.inputsCount)
			this.$refs.sequenceGrid.appendChild(circleElement)
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
			this.$refs.sequenceGrid.innerHTML = ''
		},
		toggleShowSequence () {
			this.showSequence = !this.showSequence
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
		transition: border .3s ease-in-out;
		box-sizing: border-box;

		&--show-sequence {
			border: solid 3px $color-green-dark !important;
		}
	}

	&__circle {
		position: absolute;
		background-color: rgba($color-blue, .8);
		border-radius: 50%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 24px;
		color: white;
		font-weight: 500;

		&--animated {
			background-color: rgba($color-blue, .6);
			opacity: 0;
			animation-name: pulse;
			animation-timing-function: ease-in-out;
		}
	}

	&__show-input-button {
		margin-bottom: spacing(2);
	}

	&__sequence_grid {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		left: 0;
	}
}
</style>