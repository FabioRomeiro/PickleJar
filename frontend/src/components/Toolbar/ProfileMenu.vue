<template>
    <a class="profile" @click.prevent="toggleMenu">
        <div class="profile__info">
            <span class="profile__name">{{ userName }}</span>
            <SecurityStatusBadge class="profile__status" />
        </div>
        <div class="profile__pic">
            <ImageReplace variant="white small rounded" :src="userPicutre" :name="userName" alt="Foto de perfil" />
        </div>
        <ul class="profile__menu" v-if="menuIsOpen">
            <li class="profile__menu-item">
                <a @click="logOut">
                    Log out
                </a>
            </li>
        </ul>
    </a>
</template>

<script>
import SecurityStatusBadge from '@/components/Global/SecurityStatusBadge.vue';
import ImageReplace from '@/components/Utils/ImageReplace.vue';

export default {
    name: 'ProfileMenu',
    components: {
        SecurityStatusBadge,
        ImageReplace
    },
    computed: {
        user() {
            return this.$store.getters['auth/currentUser']
        },
        userName() {
            return this.user.name
        },
        userPicutre() {
            return this.user.picture;
        }
    },
    methods: {
        toggleMenu() {
            this.menuIsOpen = !this.menuIsOpen;
        },
        logOut() {
            this.$store.dispatch('auth/logout');
            this.$router.push('/wellcome');
        }
    },
    data() {
        return {
            menuIsOpen: false
        }
    }
}
</script>

<style lang="scss">
    .profile {
        $this: &;

        text-decoration: none;
        display: flex;
        align-items: center;
        position: relative;
        cursor: pointer;

        &__menu {
            position: absolute;
            background-color: white;
            width: 230px;
            box-shadow: shadow-depth(3);
            border-radius: 3px;
            top: 48px;
            right: 0;
        }

        &__menu-item {

            width: 100%;
            display: flex;

            a {
                padding: spacing(2);
                height: 20px;
                flex-grow: 1;
                display: block;
    
                &:hover {
                    background-color: $color-green-extra-light;
                    cursor: pointer;
                }
            }

            &:first-child {
                border-top-left-radius: 3px;
                border-top-right-radius: 3px;
            }

            &:last-child {
                border-bottom-left-radius: 3px;
                border-bottom-right-radius: 3px;
            }
        }

        &__pic {
            width: 40px;
            height: 40px;
            margin-left: spacing(2);
            display: flex;
            align-items: center;
            
            img {
                border-radius: 50%;
                width: 40px;
                min-height: 40px;
                max-height: 40px;
                object-fit: cover;
            }
        }

        &__info {
            display: flex;
            flex-direction: column;
            text-align: right;
            color: white;
        }

        &__name {
            font-weight: $font-weight-semibold;
            font-size: 16px;
        }

        &__status {
            align-self: flex-end;
            margin-top: 4px;
        }
    }
</style>