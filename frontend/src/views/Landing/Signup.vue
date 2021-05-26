<template>
	<div class="signup-page">
		<h3 class="signup-page__title">Sign up a new account</h3>
		<div class="signup-page__email">
			<CustomInput
				type="email"
				label="Enter your e-mail"
				v-model="email"
			/>
		</div>
		<div class="signup-page__passimage-url">
			<CustomInput
				type="url"
				label="Link of the passimage"
				v-model="passimageUrl"
			/>
		</div>
		<div class="signup-page__passimage" v-if="passimageUrl">
			<span class="passimage-label">Click your sequence</span>
			<GraphicalInput class="passimage-input" v-model="passimageData" :passimage="passimageUrl" @update="signUp" />
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
		async signUp () {
			await api.signup(this.email, this.passimageUrl, this.passimageData)
			this.$router.push({ name: 'Login' })
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

	&__passimage-url {
		margin-top: spacing(2);
	}
}
</style>