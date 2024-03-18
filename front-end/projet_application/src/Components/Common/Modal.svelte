<script lang="ts">
    export let handleModalClick: () => void;

    const handleButtonClick = (event: MouseEvent) => {
        event.preventDefault();
        handleModalClick();
    };
</script>

<button class="slot" on:click={handleButtonClick}>
    <button class="modal" on:click|stopPropagation>
        <slot />
    </button>
</button>

<style scoped>
    .slot {
        width: 100%;
        height: 100%;
        position: fixed;
        top: 0;
        left: 0;
        background-color: rgba(0, 0, 0, 0.5); /* semi-transparent overlay */
        display: flex;
        justify-content: center;
        align-items: center;
        border: none;
    }
    .modal {
        background-color: #e5e5e5;
        width: 90%;
        max-width: 800px;
        border: none;
        border-bottom: 1px solid #00ad9a;
        border-radius: 10px;
        padding: 20px;
        box-sizing: border-box;
        z-index: 100;
    }
</style>
