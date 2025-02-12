<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <!-- left  -->
        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 rounded-lg">
                <div class="space-y-4">

                    <!-- chat 1 -->
                    <div class="p-2 bg-white border-b rounded-lg">
                        <div class="flex items-start justify-between">
                            <div class="flex items-start space-x-2">
                                <img src="../assets/images/Piglet.webp"
                                    class="w-12 h-12 rounded-full border border-gray-300" />
                                <div>
                                    <p class="text-xs font-bold">Piglet</p>
                                    <p class="pt-3 text-xs text-gray-500">Lorem ipsum dolor sit amet.</p>
                                </div>
                            </div>
                        </div>

                        <div class="text-xs text-gray-500 text-right mt-2">
                            16 seconds ago
                        </div>
                    </div>

                    <!-- chat 2 -->
                    <div class="p-2 bg-white border-b rounded-lg">
                        <div class="flex items-start justify-between">
                            <div class="flex items-start space-x-2">
                                <img src="../assets/images/tigger.jpeg"
                                    class="w-12 h-12 rounded-full border border-gray-300" />
                                <div>
                                    <p class="text-xs font-bold">Tigger</p>
                                    <p class="pt-3 text-xs text-gray-500">Lorem ipsum dolor sit amet.</p>
                                </div>
                            </div>
                        </div>

                        <div class="text-xs text-gray-500 text-right mt-2">
                            53 minutes ago
                        </div>
                    </div>

                    <!-- chat 3  -->
                    <div class="p-2 bg-white rounded-lg">
                        <div class="flex items-start justify-between">
                            <div class="flex items-start space-x-2">
                                <img src="../assets/images/Eeyore.jpeg"
                                    class="w-12 h-12 rounded-full border border-gray-300" />
                                <div>
                                    <p class="text-xs font-bold">Eeyore</p>
                                    <p class="pt-3 text-xs text-gray-500">Lorem ipsum dolor sit amet.</p>
                                </div>
                            </div>
                        </div>

                        <div class="text-xs text-gray-500 text-right mt-2">
                            1 day ago
                        </div>
                    </div>

                </div>
            </div>
        </div>

        <!-- center -->
        <div class="main-center col-span-3 space-y-4">

            <!-- texts area -->
            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="flex flex-col flex-grow p-4">
                    <!-- text 1  -->
                    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-pink-500 text-white p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                                    eiusmod.</p>
                            </div>
                            <span class="text-xs text-gray-500 leading-none">2 min ago</span>
                        </div>
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                            <img src="../assets/images/Piglet.webp" class="rounded-full" />
                        </div>
                    </div>

                    <!-- text 2  -->
                    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
                        <div>
                            <div class="bg-pink-500 text-white p-3 rounded-l-lg rounded-br-lg">
                                <p class="text-sm">Lorem ipsum dolor sit amet</p>
                            </div>
                            <span class="text-xs text-gray-500 leading-none">1 min ago</span>
                        </div>
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                            <img src="../assets/images/Piglet.webp" class="rounded-full" />
                        </div>
                    </div>

                    <!-- text 3  -->
                    <div class="flex w-full mt-2 space-x-3 max-w-md">
                        <div class="flex-shrink-0 h-10 w-10 rounded-full bg-gray-300">
                            <img src="../assets/images/pooh_baeb7dc6.jpeg" class="rounded-full" />
                        </div>
                        <div>
                            <div class="bg-gray-200 p-3 rounded-r-lg rounded-bl-lg">
                                <p class="text-sm">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                                    eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
                            </div>
                            <span class="text-xs text-gray-500 leading-none">16 sec</span>
                        </div>
                    </div>
                </div>

                <!-- type box  -->
                <div class="bg-white  rounded-lg">
                    <div class="p-4">
                    </div>

                    <div class="p-4 flex justify-between gap-2">
                        <textarea class="p-2 w-full bg-gray-100 rounded-lg" placeholder=" text me "></textarea>
                        <a href="#" class="inline-block py-4 px-6 bg-pink-800 text-white rounded-lg">send</a>
                    </div>
                </div>
            </div>


        </div>

    </div>
</template>