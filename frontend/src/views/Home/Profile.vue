<template>
	<div class="profile-page">
		<PageHeader title="Edit your profile" icon="person">
			<CustomButton class="header-button" variant="neutral" @click="$router.push('/')">
                Voltar
            </CustomButton>
		</PageHeader>
	</div>
</template>

<script>
import PageHeader from '@/components/Utils/PageHeader.vue'
import CustomButton from '@/components/Forms/CustomButton.vue'

export default {
	name: 'Profile',
	components: {
		CustomButton,
		PageHeader
	}
}
</script>

<style lang="scss" scoped>

</style>