<template>
	<div class="signup-page">
		<div class="signup-page__header">
			<a href @click.prevent="goPreviousStep" class="link" v-if="step > 1">
				Voltar
			</a>
			<h3 class="signup-page__title">Faça cadastro de uma nova conta</h3>
		</div>
		<div class="signup-page__step" v-if="step === 1">
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
						label="Nome"
						v-model="firstName"
					/>
				</div>

				<div class="signup-page__field">
					<CustomInput
						type="text"
						label="Sobrenome"
						v-model="lastName"
					/>
				</div>
			</div>

			<CustomButton @click="goNextStep" :disabled="!email || ! firstName || ! lastName">
				Configurar senha
			</CustomButton>
		</div>

		<div class="signup-page__step" v-else-if="step === 2">
			<div v-if="passwordMode">
				<PasswordInput
					v-model="password"
					@input="updatePasswordStrength"
					show-strength
				/>
				<CustomButton @click="signUp" :disabled="passwordStrength < 5">
					Continuar
				</CustomButton>
			</div>
			<div v-else>
				<div class="signup-page__field signup-page__passimage-url">
					<CustomInput
						type="url"
						label="Cole o link de uma imagem aqui"
						v-model="passimageUrl"
					/>
				</div>

				<div class="signup-page__passimage" v-if="passimageUrl">
					<span class="passimage-label">Escolha sua sequencia</span>
					<p class="passimage-description">
						Selecione 5 pontos na imagem escolhida para criar sua senha
					</p>
					<GraphicalInput class="passimage-input" v-model="passimageData" :passimage="passimageUrl" @update="signUp" with-steps />
				</div>
			</div>
		</div>

	
		<div class="signup-page__step" v-else-if="step === 3">
			<div v-if="passwordMode">
				<PasswordInput
					v-model="password"
					@input="updatePasswordStrength"
					show-strength
				/>
				<CustomButton @click="confirmSequence">
					Confirmar cadastro
				</CustomButton>
			</div>
			<div v-else>
				<div class="signup-page__field signup-page__passimage-url">
					<CustomInput
						type="url"
						v-model="passimageUrl"
						disabled
					/>
					<CustomButton @click="goPreviousStep">
						Mudar imagem
					</CustomButton>
				</div>

				<div class="signup-page__passimage">
					<span class="passimage-label">Confirme sua senha</span>
					<p class="passimage-description">
						Selecione novamente os pontos da imagem, na mesma sequencia, para confirmar sua senha
					</p>
					<GraphicalInput class="passimage-input" v-model="passimageData" :passimage="passimageUrl" @update="confirmSequence" with-steps />
				</div>
			</div>
		</div>

		<div class="signup-page__login">
			<router-link :to="`/landing${passwordMode ? '?passwordMode=true' : ''}`" class="link">
				Eu já tenho uma conta
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
		PasswordInput,
		CustomButton
	},
	computed: {
		passwordMode () {
			return !!this.$route.query.passwordMode
		}
	},
	methods: {
		async signUp () {
			await api.signup(this.email, this.passimageUrl, this.passimageData, this.firstName, this.lastName, this.password)
			this.passimageData = {}
			this.password = ''
			this.goNextStep()
		},
		async confirmSequence () {
			const user = await api.login(this.email, this.passimageData, this.password, true)
			if (user) {
				this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
						message: 'Cadastro realizado com sucesso.',
						type: 'success',
						lifeTime: 4000
				})
				if (this.passwordMode) {
					this.$router.push({ name: 'Login', query: { passwordMode: true } })
				}
				else {
					this.$router.push({ name: 'Login' })
				}
			}
			else {
				this.goPreviousStep()
				this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
						message: 'As sequências não coincidem. Tente novamente.',
						type: 'danger',
						lifeTime: 10000
				})
			}
		},
		goNextStep () {
			this.step += 1
		},
		goPreviousStep () {
			this.step -= 1
		},
		updatePasswordStrength (strength) {
			this.passwordStrength = strength
		}
	},
	data () {
		return {
			passimageData: {},
			passimageUrl: '',
			email: '',
			firstName: '',
			lastName: '',
			step: 1,
			password: '',
			passwordStrength: 0
		}
	}
}
</script>

<style lang="scss" scoped>
.signup-page {
	&__header {
		display: flex;
		align-items: center;
		margin-bottom: spacing(2);
		justify-content: space-between;
	}

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
		flex-grow: 1;

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