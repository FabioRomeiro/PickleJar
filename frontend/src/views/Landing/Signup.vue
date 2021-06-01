<template>
	<div class="signup-page">
		<h3 class="signup-page__title">Sign up a new account</h3>
		<div class="signup-page__field">
			<CustomInput
				type="email"
				label="E-mail"
				v-model="email"
			/>
		</div>

		<div class="signup-page__group-field">
			<div class="signup-page__field">
				<CustomInput
					type="text"
					label="First name"
					v-model="firstName"
				/>
			</div>

			<div class="signup-page__field">
				<CustomInput
					type="text"
					label="Last name"
					v-model="lastName"
				/>
			</div>
		</div>
		
		<div class="signup-page__field signup-page__passimage-url">
			<CustomInput
				type="url"
				label="Link of the passimage"
				v-model="passimageUrl"
			/>
		</div>

		<div class="signup-page__passimage" v-if="passimageUrl">
			<span class="passimage-label">Click your sequence</span>
			<p class="passimage-description">
				Choose 5 points on the chosen image to make it your access pass
			</p>
			<GraphicalInput class="passimage-input" v-model="passimageData" :passimage="passimageUrl" @update="signUp" with-steps />
		</div>

		<div class="signup-page__login">
			<router-link to="/landing" class="link">
				I already have an account
			</router-link>
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
			await api.signup(this.email, this.passimageUrl, this.passimageData, this.firstName, this.lastName)
			this.$router.push({ name: 'Login' })
		}
	},
	data () {
		return {
			passimageData: {},
			passimageUrl: '',
			email: '',
			firstName: '',
			lastName: ''
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

		.passimage-description {
			margin-bottom: spacing(2);
			font-weight: 500;
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

	&__field {
		margin-bottom: spacing(2);
		flex-grow: 1;
	}

	&__group-field {
		display: flex;
		align-items: center;
		gap: spacing(2);
	}

	&__login {
		margin-top: spacing(2);
	}
}
</style>