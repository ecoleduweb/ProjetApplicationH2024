

export interface Offre { 
    titre: string; // titre de l'offre
    lieu: string; // lieu de travail
    dateEntreeFonction: string // date d'entrée en fonction
    dateLimitePostuler: string // date limite pour postuler
    salaire: number; // salaire de lheure 
    typeEmplois: string; // si stage vrai sinon faux
    heures: number; // nombre d'heures par semaine  
    programme: string; // le programme visée par l'offre
    conciliation: boolean; // employeur conciliant ou non
    urgente: boolean; // si l'offre est urgente
    lien: string; // lien vers l'offre ou site web de l'employeur
    description: string; // description de l'offre
    courrielContact: string; // courriel de la personne à contacter
    active: boolean; // si l'offre est active ou non
}