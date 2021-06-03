<template>
    <div class="alert" v-if="alertAlive">
        <div class="alert__content" :class="`alert__content--${ options.type }`">
            <i class="material-icons alert__icon">{{ options.icon }}</i>

            <p class="alert__message">{{ options.message }}</p>
            
            <a href @click.prevent="killAlert()" class="alert__close-button" v-if="!options.cantClose">
                <i class="material-icons icon">close</i>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Alert',
    mounted() {
        this.$eventBus.on(this.$eventKeys.CALL_ALERT, options => {
            if (!options.message) {
                throw new Error('The Alert component need a message')
            }

            this.options = {
                ...this.options,
                ...options
            }

            this.alertAlive = true
            this.alertTimeout = setTimeout(this.killAlert, this.options.lifeTime)
        })
    },
    methods: {
        killAlert() {
            if (this.alertTimeout) {
                clearTimeout(this.alertTimeout)
                this.alertTimeout = null;
            }

            this.alertAlive = false;
            this.options = this.getDefaultOptions();
        },
        getDefaultOptions() {
            return {
                icon: 'done',
                type: 'info',
                cantClose: false,
                lifeTime: 2000
            }
        }
    },
    data() {
        return {
            alertAlive: false,
            options: this.getDefaultOptions(),
            alertTimeout: null
        }
    }
}
</script>

<style lang="scss" scoped>
    @keyframes fade-in {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .alert {
        
        $this: &;

        position: fixed;
        top: 40px;
        left: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 5;
        width: 100vw;
        opacity: 0;
        animation: fade-in .3s ease-in forwards;

        &__icon {
            font-size: 16px;
            margin-right: spacing(1);
        }

        &__close-button {
            
            margin-left: spacing(1);

            .icon {
                font-size: 16px;
                margin-right: 0;
            }
        }

        &__message {
            flex-grow: 1;
            font-size: 12px;
        }

        &__content {
            min-width: 40vw;
            max-width: 50vw;
            height: 30px;
            border-radius: 4px;
            display: flex;
            align-items: center; 
            border: solid 1px;
            box-shadow: shadow-depth(5);
            padding: spacing(1);
            
            &--info {
                background-color: $color-blue-light;
                border-color: $color-blue;

                #{$this}__close-button,
                #{$this}__icon {
                    &, .icon {
                        color: $color-blue;
                    }
                }
            }
            
            &--success {
                background-color: $color-green-extra-light;
                border-color: $color-green-dark;

                #{$this}__close-button,
                #{$this}__icon {
                    &, .icon {
                        color: $color-green-dark;
                    }
                }
            }
            
            &--danger {
                background-color: $color-red-extra-light;
                border-color: $color-red-dark;

                #{$this}__close-button,
                #{$this}__icon {
                    &, .icon {
                        color: $color-red-dark;
                    }
                }
            }
        }
    }
</style>