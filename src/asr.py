import whisper
from jiwer import wer

model = whisper.load_model("base")

audio_dataset = {
    "audio.wav": "Hello open minds. Get ready. This project is your first step into the world of multimedia systems, where images, audio and artificial intelligence come together to do some pretty cool things.",
    "audio1.wav": "Salut c'est pour quand la date limite du projet.",
    "audio2.wav": "Artificial intelligence has become one of the most influential technologies of the twenty-first century. Researchers and engineers are constantly developing new algorithms capable of understanding human language, recognizing speech, and analyzing large amounts of data in real time. However, evaluating the performance of these systems requires carefully designed experiments. For example, a speech recognition model must be tested using audio recordings with different accents, speaking speeds, and...",
    "audio3.wav": "Au cours des 20 dernières années, les progrès en intelligence artificielle ont profondément transformé la manière dont les machines interprètent le langage humain. Par exemple, certains systèmes modernes de reconnaissance vocale peuvent analyser plusieurs milliers de mots en moins de 5 secondes, tout en maintenant un taux d’erreur inférieur à 10 %. Cependant, l’évaluation de ces technologies reste un défi important. Les chercheurs doivent tester leurs modèles sur différents types d’enregistrements.",
    "audio4.wav": "Technology is an important part of everyday life. People use computers and smartphones to communicate, study, and work. In recent years, artificial intelligence has helped improve many tools, including speech recognition systems."
}

# Creating a list to store the errors of each audio file, initially the list is empty
WER_List = []

# Loop through the dataset and compare the converted text to the text in the dictionary
for i, (file, reference) in enumerate(audio_dataset.items()):
    # The model listens to the audio and returns the text it thinks it heard
    prediction = model.transcribe("data/" + file)["text"]

    # Calculate the error of each audio file 
    error = wer(reference, prediction)

    # Add the error to the list WRE_List
    WER_List.append(error)
    
    # Print the error of each audio file in percentage
    print(f"File {i}: {file}, WER: {error * 100:.2f}%")

