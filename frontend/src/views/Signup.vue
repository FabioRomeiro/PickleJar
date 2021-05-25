<template>
	<div class="signup-page">
		<div class="signup-page__box">
			<div class="signup-page__email">
				<CustomInput
					type="email"
					label="Enter your e-mail"
					v-model="email"
				/>
				<CustomInput
					type="url"
					label="Link of the passimage"
					v-model="passimageUrl"
				/>
			</div>
			<div class="signup-page__passimage" v-if="passimageUrl">
				<GraphicalInput v-model="passimageData" :passimage="passimageUrl" @update="cadastrar" />
			</div>
		</div>
	</div>
</template>

<script>
import api from 'Apijs'
import CustomInput from '@/components/Forms/CustomInput'
import GraphicalInput from '@/components/Forms/GraphicalInput'

export default {
	components: {
		CustomInput,
		GraphicalInput
	},
	methods: {
		cadastrar () {
			api.signup(this.email, this.passimageUrl, this.passimageData)
		}
	},
	data () {
		return {
			passimageData: {},
			passimageUrl: '',
			email: ''
		}
	}
}
</script>

<style lang="scss" scoped>
.signup-page {
	width: 100%;
	height: 100vh;
	background-color: $color-green;
	display: flex;
	align-items: center;
	justify-content: center;

	&__box {
		width: 600px;
		background-color: white;
		padding: spacing(2);
		border-radius: 3px;
	}

	&__passimage {
		display: flex;
		justify-content: center;
		margin-top: spacing(2)
	}
}
</style>