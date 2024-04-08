import boto3

class AudioService:
    def __init__(self):
        self.polly_client = boto3.client('polly')
        self.translate_client = boto3.client('translate')
        
    def generate_audio(self, text, target_lang):
        if not text:
            raise ValueError("No text provided")

        if target_lang != "en-US":
            try:
                translation = self.translate_client.translate_text(
                    Text=text,
                    SourceLanguageCode='en',
                    TargetLanguageCode=target_lang.split('-')[0]
                )
                text = translation['TranslatedText']
            except Exception as e:
                raise ValueError(f"Translation error: {str(e)}")

        try:
            response = self.polly_client.synthesize_speech(
                Text=text,
                OutputFormat='mp3',
                VoiceId='Joanna'
            )
            return response['AudioStream'].read()
        except Exception as e:
            raise ValueError(f"Speech synthesis error: {str(e)}")
