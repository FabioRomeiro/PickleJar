<template>
	<div class="login-page">
		<h3 class="login-page__title">Entre na sua conta</h3>
		<div class="login-page__email">
			<CustomInput
				class="email-input"
				type="email"
				label="E-mail"
				v-model="email"
				:disabled="passimageUrl && !passwordMode"
			/>
			<div v-if="!passwordMode">
				<CustomButton v-if="!passwordStep" @click="goToPasswordStep" class="email-submit">
					Continuar
				</CustomButton>
				<CustomButton v-else @click="changeEmail" class="email-submit">
					Mudar de e-mail
				</CustomButton>
			</div>
		</div>
		<div v-if="passwordStep || passwordMode">
			<div class="login-page__passimage" v-if="!passwordMode">
				<span class="passimage-label">Clique nos pontos com a sequencia cadastrada</span>
				<GraphicalInput class="passimage-input" v-model="passimageData" :passimage="passimageUrl" @update="logIn" />
			</div>
			<div v-else>
				<PasswordInput v-model="password" />
				<CustomButton @click="logIn">
					Entrar
				</CustomButton>
			</div>
		</div>
		<div class="login-page__signup">
			<router-link :to="`/landing/signup${passwordMode ? '?passwordMode=true' : ''}`" class="link">
				Não tenho uma conta ainda
			</router-link>
		</div>
	</div>
</template>

<script>
import api from 'Apijs'
import CustomInput from '@/components/Forms/CustomInput'
import CustomButton from '@/components/Forms/CustomButton'
import GraphicalInput from '@/components/Forms/GraphicalInput'
import PasswordInput from '@/components/Forms/PasswordInput'

export default {
	components: {
		CustomInput,
		GraphicalInput,
		CustomButton,
		PasswordInput
	},
	computed: {
		passwordMode () {
			return !!this.$route.query.passwordMode
		}
	},
	methods: {
		async goToPasswordStep () {
			if (!this.passwordMode) {
				await this.loadImagepass()
			}
			this.passwordStep = true
		},
		changeEmail () {
			this.passwordStep = false
			this.resetPassimage()
		},
		async logIn () {
			try {
				const params = {
					email: this.email,
				}
				if (this.passwordMode) {
					params.password = this.password
				}
				else {
					params.passimageData = this.passimageData
				}
				await this.$store.dispatch('auth/login', params)
				const user = this.$store.getters['auth/currentUser']
				if (user) {
					this.$router.push({ name: 'Home' })
				}
				else {
					this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
						message: 'Email ou senha incorreta.',
						type: 'danger',
						lifeTime: 10000
					})
				}
			}
			catch (e) {
				this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
						message: 'Sequencia incorreta. Tenha certeza de que clicou nos lugares corretos.',
						type: 'danger',
						lifeTime: 4000
				})
			}
		},
		async loadImagepass () {
			try {
				const { image_url } = await api.getPassImage(this.email)
				this.passimageUrl = image_url
			} 
			catch (e) {
				this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
						message: 'This e-mail is not associated with any account',
						type: 'danger',
						lifeTime: 4000
				})
			}
		},
		resetPassimage () {
			this.passimageUrl = null
		}
	},
	data () {
		return {
			passimageData: {},
			passimageUrl: null,
			passwordStep: false,
			password: '',
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