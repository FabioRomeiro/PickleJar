<template>
	<div class="login-page">
		<h3 class="login-page__title">Log into your account</h3>
		<div class="login-page__email">
			<CustomInput
				class="email-input"
				type="email"
				label="E-mail"
				v-model="email"
				:disabled="passimageUrl"
			/>
			<CustomButton v-if="!passimageUrl" @click="loadImagepass" class="email-submit">
				Continue
			</CustomButton>
			<CustomButton v-else @click="resetPassimage" class="email-submit">
				Change e-mail
			</CustomButton>
		</div>
		<div class="login-page__passimage" v-if="passimageUrl">
			<span class="passimage-label">Click your sequence</span>
			<GraphicalInput class="passimage-input" v-model="passimageData" :passimage="passimageUrl" @update="logIn" />
		</div>
		<div class="login-page__signup">
			<router-link to="/landing/signup" class="link">
				I don't have an account
			</router-link>
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
		async logIn () {
			const user = await api.login(this.email, this.passimageData)
			if (user) {
				this.$router.push({ name: 'Home' })
			}
		},
		async loadImagepass () {
			const { image_url } = await api.getPassImage(this.email)
			this.passimageUrl = image_url
		},
		resetPassimage () {
			this.passimageUrl = null
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

	&__email {
		display: flex;
		align-items: center;

		@media (max-width: 360px) {
			flex-direction: column;
			width: 100%;
		}

		.email-input {
			flex-grow: 1;

			@media (max-width: 360px) {
				width: 100%;
			}
		}

		.email-submit {
			margin-top: spacing(2);
			
			@media (min-width: 361px) {
				margin-left: spacing(2);
			}
		}
	}

	&__passimage {
		display: flex;
		flex-direction: column;
		margin-top: spacing(2);

		.passimage-label {
			margin-bottom: spacing(1);
		}

		.passimage-input {
			align-self: center;
		}
	}

	&__title {
		font-size: 24px;
		font-weight: 500;
		text-align: center;
		margin-bottom: spacing(2);

		@media (max-width: 360px) {
			font-size: 18px;
		}
	}

	&__signup {
		margin-top: spacing(2);
	}
}
</style>