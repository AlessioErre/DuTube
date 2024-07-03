
<?php
class Wav{
  // Proprietà private
  private $wav = "wav";
  private $link;

  // Costruttore
  public function __construct($wav, $link) {
    $this->wav = $wav;
    $this->link = $link;
  }

  // Metodo pubblico per accedere alla proprietà nome
  public function getWav() {
    return $this->wav;
  }

  // Metodo pubblico per accedere alla proprietà cognome
  public function getLink() {
    return $this->link;
  }


   public function WAvAudio(){
      system("python3 /home/black-jack/05-Script/03-Altrui/yt-dlp/yt_dlp/__main__.py -x --audio-format " . $this->wav . " -P /home/black-jack/05-Script/DuTube/Downloads " . $this->link);
   }}

$wav = "wav";
$audio = new Wav($wav, $argv[1]);
$audio->WavAudio();

