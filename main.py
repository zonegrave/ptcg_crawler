import sys
import time
import os
from pathlib import Path
from single_card_download import SingleCardDownloader
from deck_decoder import DeckDecoder
from pdf_builder import build_pdf_with_cards


def make_deck_file_pdf(deck_file, fetch_img_sleep = 1):
    i_decoder = DeckDecoder(deck_file)
    card_images = []
    for copies, seriers_name, card_idx_in_seriers in i_decoder.cards:
        downloader = SingleCardDownloader(seriers_name, card_idx_in_seriers)
        image_path = downloader.get_img_hd()
        if downloader.url_requested:
            time.sleep(fetch_img_sleep)
        for i in range(copies):
            card_images.append(image_path)
    deck_stem = Path(deck_file).stem
    pdf = build_pdf_with_cards(deck_stem, card_images)
    pdf.output("decks/%s.pdf"%deck_stem, "F")


if __name__ == "__main__":
    # deck_file = sys.argv[1]
    # make_deck_file_pdf(deck_file)
    files = os.listdir("./decks")
    for file in files:
        if Path(file).suffix == ".deck":
            print(">>>>>>>>>>> deck: %s"%file)
            make_deck_file_pdf("./decks/%s"%file)
    

    