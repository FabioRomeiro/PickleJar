<template>
	<div class="profile-page">
		<PageHeader title="Edit your profile" icon="person">
			<CustomButton class="header-button" variant="neutral" @click="$router.push('/')">
				Voltar
			</CustomButton>
		</PageHeader>
		<div class="profile-page__form">
			<CustomInput v-model="email" class="profile-page__input" label="E-mail" />
			<div class="profile-page__input-group">
				<CustomInput v-model="firstName" class="profile-page__input" label="First name" />
				<CustomInput v-model="lastName" class="profile-page__input" label="Last name" />
			</div>
			<CustomInput v-model="passimage" class="profile-page__input" label="Passimage" />
			<GraphicalInput class="passimage-input" v-model="passimageData" :passimage="passimage" with-steps />
			<CustomButton class="profile-page__submit-button" @click="updateProfile">
				Update profile
			</CustomButton>
		</div>
	</div>
</template>

<script>
import api from 'Apijs'

import PageHeader from '@/components/Utils/PageHeader.vue'
import CustomButton from '@/components/Forms/CustomButton.vue'
import CustomInput from '@/components/Forms/CustomInput.vue'
import GraphicalInput from '@/components/Forms/GraphicalInput'

export default {
	name: 'Profile',
	components: {
		CustomButton,
		CustomInput,
		PageHeader,
		GraphicalInput
	},
	mounted () {
		const user = this.$store.getters['auth/currentUser']
		this.firstName = user.first_name
		this.lastName = user.last_name
		this.email = user.email
		this.passimage = user.passimage_url
	},
	data () {
		return {
			firstName: null,
			lastName: null,
			email: null,
			passimage: null,
			passimageData: null
		}
	},
	methods: {
		async updateProfile () {
			let user = {
				first_name: this.firstName,
				last_name: this.lastName,
				passimage_url: this.passimage
			}
			if (this.passimageData) {
				user.pass_data = JSON.stringify({
					grid_size: this.passimageData.gridSize,
					coords: this.passimageData.inputs
				})
			}
			try {
				await api.saveUser(user)
				this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
					message: 'Informações do perfil salvas com sucesso',
					type: 'success',
					lifeTime: 4000
				})
			} catch (e) {
				this.$eventBus.emit(this.$eventKeys.CALL_ALERT, {
					message: 'Ocorreu um erro ao salvar as informações do perfil',
					type: 'danger',
					lifeTime: 4000
				})
			}
		}
	}
}
</script>

<style lang="scss" scoped>
	.profile-page {
		&__input-group {
			display: flex;
			align-items: center;
			gap: spacing(2);
		}

		&__input {
			flex-grow: 1;
			margin-bottom: spacing(2);
		}

		&__form {
			max-width: 600px;
			margin: spacing(2) auto spacing(4) auto;
		}

		&__submit-button {
			margin: spacing(2) auto;
			display: block;
		}
	}
</style>