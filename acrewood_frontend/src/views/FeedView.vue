<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <!-- center -->
        <div class="main-center col-span-3 space-y-4 mx-20">
            <!-- posting box area  -->
            <div class="p-4 pb-0 bg-white border border-gray-200 rounded-lg">
                <form v-on:submit.prevent="submitForm" method="post">
                    <!-- post box -->
                    <div class="p-4 pb-0">
                        <textarea v-model="body" class="p-8 w-full bg-gray-100 rounded-lg" placeholder="What's on your mind? "></textarea>
                    </div>
                    <!-- post buttons  -->
                    <div class="py-4 px-8 border-t border-gray-100 flex justify-between">
                        <a href="#" class="inline-block py-2 px-4 bg-gray-600 text-white rounded-lg">Attach</a>
                        <button class="inline-block py-2 px-4 bg-pink-600 text-white rounded-lg">Post</button>
                    </div>
                </form>
            </div>


            <!-- Functional Posts -->
            <div class="p-4 bg-white border border-gray-200 rounded-lg" 
            v-for="post in posts" v-bind:key="post.id">
                
                <!-- post header -->
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="../assets/images/pooh_baeb7dc6.jpeg"
                            class="w-12 h-12 rounded-full  border border-gray-300" />
                        <p><strong>{{ post.created_by.name }}</strong></p>
                    </div>
                    <p class="text-gray-600">{{ post.created_at_formatted }} ago</p>
                </div>

                <!-- post body -->
                <p>{{ post.body }}</p>

                <!-- post footer -->
                <div class="mt-6 flex justify-between">
                    <!-- left side -->
                    <div class="flex space-x-6">
                        <!-- likes icon -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                            </svg>
                            <span class="text-gray-500 text-xs">82 likes</span>
                        </div>
                        <!-- comments icon  -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>
                            <span class="text-gray-500 text-xs">6 comments</span>
                        </div>
                    </div>


                    <!-- right side -->
                    <div>
                        <!-- options dots -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
                        </svg>
                    </div>
                </div>
            </div>


            <!-- post 1 area -->
            <div class="p-4 bg-white border border-gray-200 rounded-lg">


                <!-- post header -->
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="../assets/images/pooh_baeb7dc6.jpeg"
                            class="w-12 h-12 rounded-full  border border-gray-300" />
                        <p><strong>Winnie The Pooh</strong></p>
                    </div>
                    <p class="text-gray-600">18 minutes ago</p>
                </div>
                <!-- post image -->
                <img src="../assets/images/academia_(4).jpg" class="w-full h-18 rounded-lg">



                <!-- post footer -->
                <div class="my-6 flex justify-between">


                    <!-- left side -->
                    <div class="flex space-x-6">
                        <!-- likes icon -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                            </svg>
                            <span class="text-gray-500 text-xs">82 likes</span>
                        </div>
                        <!-- comments icon  -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>
                            <span class="text-gray-500 text-xs">6 comments</span>
                        </div>
                    </div>


                    <!-- right side -->
                    <div>
                        <!-- options dots -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
                        </svg>
                    </div>
                </div>
            </div>


            <!-- post 2 area -->
            <div class="p-4 bg-white border border-gray-200 rounded-lg">


                <!-- post header -->
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-6">
                        <img src="../assets/images/pooh_baeb7dc6.jpeg"
                            class="w-12 h-12 rounded-full  border border-gray-300" />
                        <p><strong>Winnie The Pooh</strong></p>
                    </div>
                    <p class="text-gray-600">34 minutes ago</p>
                </div>
                <!-- post image -->
                <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Ipsa suscipit doloremque fugiat nisi iusto,
                    laborum enim odio dolorem eos dolores voluptates quaerat, quos veniam in temporibus dolore officiis
                    voluptas incidunt.</p>


                <!-- post footer -->
                <div class="my-6 flex justify-between">


                    <!-- left side -->
                    <div class="flex space-x-6">
                        <!-- likes icon -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" />
                            </svg>
                            <span class="text-gray-500 text-xs">92 likes</span>
                        </div>
                        <!-- comments icon  -->
                        <div class="flex items-center space-x-2">
                            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                                stroke="currentColor" class="w-6 h-6">
                                <path stroke-linecap="round" stroke-linejoin="round"
                                    d="M12 20.25c4.97 0 9-3.694 9-8.25s-4.03-8.25-9-8.25S3 7.444 3 12c0 2.104.859 4.023 2.273 5.48.432.447.74 1.04.586 1.641a4.483 4.483 0 01-.923 1.785A5.969 5.969 0 006 21c1.282 0 2.47-.402 3.445-1.087.81.22 1.668.337 2.555.337z" />
                            </svg>
                            <span class="text-gray-500 text-xs">15 comments</span>
                        </div>
                    </div>


                    <!-- right side -->
                    <div>
                        <!-- options dots -->
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                            stroke="currentColor" class="w-6 h-6">
                            <path stroke-linecap="round" stroke-linejoin="round"
                                d="M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z" />
                        </svg>
                    </div>
                </div>
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

export default {
    name: 'FeedView',

    components: {
        PeopleYouMayKnow,
        Trends,
    },

    data() {
        return {
            posts: [],
            body: '',
        }
    },

    mounted() {
        this.getFeed()
    },

    methods: {
        getFeed() {
            axios
                .get('/api/posts/')
                .then(response => {
                    console.log('data', response.data)

                    this.posts = response.data
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