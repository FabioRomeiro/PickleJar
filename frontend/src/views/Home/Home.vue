<template>
	<div class="home">
		<Toolbar />
		<div class="home__wrapper">
			<router-view/>
		</div>
		<CredentialWorkspace />
	</div>
</template>

<script>
import Toolbar from '@/components/Toolbar/Toolbar.vue'
import CredentialWorkspace from '@/components/CredentialWorkspace/CredentialWorkspace.vue'

export default {
	name: 'Home',
	components: {
		Toolbar,
		CredentialWorkspace
	},
	created () {
		const self = this
		const ws = new WebSocket(`ws://picklejar-api.fabioromeiro.dev/ws/user/`)
		ws.onmessage = evt => {
			const data = JSON.parse(evt.data)
			if (data.type === 'send_logout') {
					self.$router.push({ name: 'Landing' })
			}
			else if (data.type === 'send_updated_user') {
					self.$store.commit('auth/SET_CURRENT_USER', data.user)
			}
		}
	}
};
</script>

<style lang="scss" scoped>
	.home {
		&__wrapper {
			max-width: 1080px;
			width: 90%;
			margin: 0 auto;
			margin-top: spacing(5);
		}
	}
</style>