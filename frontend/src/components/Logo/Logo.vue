<template>
    <component :is="linkOff ? 'div' : 'router-link'" to="/" class="logo" :class="variants">
        <LogoSvg :size="size" class="logo__draw" />
        <div class="logo__text">
            <h1 class="title">Pickle Jar</h1>
            <h2 class="subtitle">
                <span>Lock it </span>
                <strong>Safe</strong>
            </h2>
        </div>
    </component>
</template>

<script>
import LogoSvg from '@/components/Logo/LogoSvg.vue';

export default {
    name: 'Logo',
    props: {
        size: String,
        variant: String,
        linkOff: Boolean
    },
    components: {
        LogoSvg
    },
    computed: {
        variants() {
            return [
                `logo--${this.size}`,
                `logo--${this.variant}`
            ]
        }
    }
}
</script>

<style lang="scss">
    .logo {
        $this: &;

        display: flex;
        align-items: center;

        &__text {
            margin-left: spacing(2);
            font-weight: $font-weight-light;
            color: white;

            strong {
                font-weight: $font-weight-regular;
            }

            .title {
                font-weight: $font-weight-semibold;
                font-size: 16px;
                margin-bottom: 4px;
            }
        }

        &--big {
            #{$this}__text {
                
                .title {
                    font-size: 28px;
                }
                
                .subtitle {
                    font-size: 20px;
                }
            }
        }

        &--badge {

            #{$this}__draw {
                background-color: $color-green;
                padding: spacing(1);
                border-radius: 3px;
            }

            #{$this}__text {
                color: $color-green;
            }
        }
    }
</style>