<script lang="ts">
    import type { Emploi } from "../Models/Emploi";
    export let emploi: Emploi;
    export let handleModalClick: () => void;

    const handleButtonClick = (event: MouseEvent) => {
        event.preventDefault();
        handleModalClick();
    };
</script>

<button class="slot" on:click={handleButtonClick}>
    <button class="modal" on:click|stopPropagation>
        <div class="containre">
            <div class="info">
                <p class="text">{emploi.titre}</p>
                <p class="text">{emploi.entreprise}</p>
                <p class="text">{emploi.dateFin}</p>
                <p class="text">{emploi.description}</p>
            </div>
        </div>
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
    .info {
        font-size: 1.3rem;
        margin-bottom: 20px;
        color: black;
    }
    .text {
        margin-right: 10px;
    }
    .containre {
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
</style>
