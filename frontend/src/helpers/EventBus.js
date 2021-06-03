class EventBus {
    constructor(){
        this.events = {}
    }

    on(eventName, fn, deleteOld) {
        if (deleteOld) {
            this.off(eventName, fn)
        }
        this.events[eventName] = this.events[eventName] || []
        this.events[eventName].push(fn)
    }

    off(eventName, fn) {
        if (this.events[eventName]) {
            for (var i = 0; i < this.events[eventName].length; i++) {
                if (this.events[eventName][i] === fn) {
                    this.events[eventName].splice(i, 1)
                    break
                }
            }
        }
    }

    emit(eventName, data) {
        if (this.events[eventName]) {
            this.events[eventName].forEach(function(fn) {
                fn(data)
            })
        }
    }
}

export const eventBus = new EventBus()

export const EVENTS = {
    ADD_CREDENTIAL: 'ADD_CREDENTIAL',
    EDIT_CREDENTIAL: 'EDIT_CREDENTIAL',
    VIEW_CREDENTIAL: 'VIEW_CREDENTIAL',
    CALL_ALERT: 'CALL_ALERT'
}
