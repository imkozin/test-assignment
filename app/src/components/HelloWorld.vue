<!-- Дан фрагмент кода некоего приложения, в котором можно создавать сущности с полями title и body (для простоты - сообщения с заголовком). Предполагается, что интерфейс отображает эти сообщения на странице после нажатия кнопки Create. Какие ошибки допустил разработчик в данном фрагменте кода?
<template>
    <div class="app">
        <form>
            <h1>Creating item</h1>
            <input 
                v-bind:value="title" 
                class="input" 
                type="text" 
                placeholder="Title"
            >
            <input 
                v-bind:value="body" 
                class="input" 
                type="text" 
                placeholder="Body"
            >
            <button 
                class="btn" 
                @click="createItem"
            >
                Create
            </button>
        </form>
        <div class="item" v-for"item in items">
            <div>Title: {{ item.title }}</div>
            <div>Body:  {{ item.body }}</div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [
                {
                    id: 1, 
                    title: "Some title 1", 
                    body: "Some body 1"
                },
                {
                    id: 2, 
                    title: "Some title 2", 
                    body: "Some body 2"
                }
            ],
            title: '',
            body: '',
        }
    },
    methods: {
        createItem(event) {
            const newItem = {
                id: Date.now(),
                title: this.title,
                body: this.body,
            }
            this.items.push(newPost);
            this.title = '';
            this.body = '';
        }
    }
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
</style> -->

<template>
    <div class="app">
        <form @submit.prevent="createItem">
            <h1>Creating item</h1>
            <input 
                v-model="title" 
                class="input" 
                type="text" 
                placeholder="Title"
            >
            <input 
                v-model="body" 
                class="input" 
                type="text" 
                placeholder="Body"
            >
            <button 
                class="btn" 
                type="submit"
            >
                Create
            </button>
        </form>
        <div class="item" v-for="item in items">
            <div>Title: {{ item.title }}</div>
            <div>Body:  {{ item.body }}</div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            items: [
                {
                    id: 1, 
                    title: "Some title 1", 
                    body: "Some body 1"
                },
                {
                    id: 2, 
                    title: "Some title 2", 
                    body: "Some body 2"
                }
            ],
            title: '',
            body: '',
        }
    },
    methods: {
        createItem() {
            const newItem = {
                id: Date.now(),
                title: this.title,
                body: this.body,
            }
            this.items.push(newItem);
            this.title = '';
            this.body = '';
            console.log('items', this.items);
        }
    }
}
</script>

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
</style>