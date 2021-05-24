<template>
	<div class="login-page">
		<div class="login-page__box">
			<div class="login-page__email">
				<CustomInput
					type="email"
					label="Enter your e-mail"
					v-model="email"
				/>
				<CustomButton @click="loadImagepass">
					Go
				</CustomButton>
			</div>
			<div class="login-page__passimage" v-if="passimageUrl">
				<GraphicalInput v-model="passimageData" :passimage="passimageUrl" @update="entrar" />
			</div>
		</div>
	</div>
</template>

<script>
import api from 'Apijs'
import CustomInput from '@/components/Forms/CustomInput'
import CustomButton from '@/components/Forms/CustomButton'
import GraphicalInput from '@/components/Forms/GraphicalInput'

export default {
	components: {
		CustomInput,
		GraphicalInput,
		CustomButton
	},
	methods: {
		entrar () {
			api.login(this.email, this.passimageData)
		},
		async loadImagepass () {
			const { image_url } = await api.getPassImage(this.email)
			this.passimageUrl = image_url
		}
	},
	data () {
		return {
			passimageData: {},
			passimageUrl: null,
			email: ''
		}
	}
}
</script>

<style lang="scss" scoped>
.login-page {
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