<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <!-- left -->
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <div
                    class="w-30 h-30 mb-6 flex justify-center items-center border border-gray-300 overflow-hidden mx-auto">
                    <img src="../assets/images/pooh_baeb7dc6.jpeg" class="w-full h-full object-cover" />
                </div>

                <p><strong>{{ user.name }}</strong></p>

                <div class="mt-6 flex space-x-8 justify-around">
                    <p class="text-xs text-gray-500">180 friends</p>
                    <p class="text-xs text-gray-500">11 posts</p>
                </div>
            </div>
        </div>


        <!-- center -->
        <div class="main-center col-span-2 space-y-4">
            <!-- posting box area  -->
            <div class="p-4 pb-0 bg-white border border-gray-200 rounded-lg"
                v-if="userStore.user.id === user.id"
            >
                <form v-on:submit.prevent="submitForm" method="post">
                    <!-- post box -->
                    <div class="p4">
                        <textarea v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What's on your mind? "></textarea>
                    </div>
                    <!-- post buttons  -->
                    <div class="py-4 px-8 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-2 px-4 bg-gray-600 text-white rounded-lg">Attach</a>
                        <button class="inline-block py-2 px-4 bg-pink-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>


            <div 
                class="p-4 bg-white border border-gray-200 rounded-lg"
                v-for="post in posts"
                v-bind:key="post.id"
            >
                <FeedItem v-bind:post="post" />
            </div>

        </div>


        <!-- right -->
        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue'
import Trends from '../components/Trends.vue'
import FeedItem from '../components/FeedItem.vue'
import { useUserStore } from '@/stores/user'


export default {
    name: 'ProfileView',

    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    components: {
        PeopleYouMayKnow,
        Trends,
        FeedItem
    },

    data() {
        return {
            posts: [],
            user: {},
            body: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    watch: { 
        '$route.params.id': {
            handler: function() {
                this.getFeed()
            },
            deep: true,
            immediate: true
        }
    },

    methods: {
        getFeed() {
            axios
                .get(`/api/posts/profile/${this.$route.params.id}/`)
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data.posts
                    this.user = response.data.user
                })
                .catch(error => {
                    console.log('error', error)
                })
        },

        submitForm() {
            console.log('submitForm', this.body)

            axios
                .post('/api/posts/create/', {
                    'body': this.body
                })
                .then(response => {
                    console.log('data', response.data)

                    this.posts.unshift(response.data)
                    this.body = ''
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }
}
</script>