#!/usr/bin/env python
#coding: utf8

"""LotoXML

A class that generates XML files for each 
Caixa Econômica Federal's game, using 
previously generated CSV files.

"""

__author__ = "José Lopes de Oliveira Júnior"
__license__ = "GPLv3+"


import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom


class LotoXML(object):
   
    """Main class.
    
    Parses CSV files generating XML version of them.
   
    """
    
    def __init__(self, url, file_output):
        self.comment = "Generated with LotoParser."
        self.id = "id"
        
        # Opens CSV file for reading using csv module.
        self.file_csv = open(url, "r")
        self.reader = csv.reader(self.file_csv, delimiter=";")
        
        self.file_xml = open(file_output, "w")  # Can raise OSError.
        
        if file_output.find("megasena") + 1:
            # Create XML file's header and root.
            self.root = Element("megasena", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/megasena.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.megasena(self.root, self.id, row)
            
        elif file_output.find("lotofacil") + 1:
            # Create XML file's header and root.
            self.root = Element("lotofacil", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/lotofacil.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.lotofacil(self.root, self.id, row)
            
        elif file_output.find("quina") + 1:
            # Create XML file's header and root.
            self.root = Element("quina", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/quina.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.quina(self.root, self.id, row)
            
        elif file_output.find("lotomania") + 1:
            # Create XML file's header and root.
            self.root = Element("lotomania", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/lotomania.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.lotomania(self.root, self.id, row)
            
        elif file_output.find("duplasena") + 1:
            # Create XML file's header and root.
            self.root = Element("duplasena", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/duplasena.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.duplasena(self.root, self.id, row)
            
        elif file_output.find("federal") + 1:
            # Create XML file's header and root.
            self.root = Element("federal", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/federal.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.federal(self.root, self.id, row)
            
        elif file_output.find("lotogol") + 1:
            # Create XML file's header and root.
            self.root = Element("lotogol", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/lotogol.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.lotogol(self.root, self.id, row)
            
        elif file_output.find("loteca") + 1:
            # Create XML file's header and root.
            self.root = Element("loteca", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/loteca.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.loteca(self.root, self.id, row)
            
        elif file_output.find("timemania") + 1:
            # Create XML file's header and root.
            self.root = Element("timemania", 
                {"xmlns:xsi":"http://joselopes.org",
                "xsi:noNamespaceSchemaLocation":"../xsd/timemania.xsd"})
            self.root.append(Comment(self.comment))
            
            # Each row is a XML concourse entry with its elements.
            for row in self.reader:
                self.timemania(self.root, self.id, row)
            
        else:
            raise ValueError
        
        # Writes data into file.
        self.file_xml.write(self.to_string(self.root).encode("utf-8"))

        # Closes all files.
        self.file_csv.close()
        self.file_xml.close()
    
    
    def to_string(self, element, indent="    "):
        """Return a pretty-printed XML string for the Element.
        
        Made by Doug Hellmann.
        
        """
        rough_string = tostring(element, "utf-8")
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent=indent)
    
    def megasena(self, root, identifier, row):
        """Process each MegaSena's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
       
        ball_01 = SubElement(concourse, "ball", {identifier:"1"})
        ball_01.text = row[2]
        ball_02 = SubElement(concourse, "ball", {identifier:"2"})
        ball_02.text = row[3]
        ball_03 = SubElement(concourse, "ball", {identifier:"3"})
        ball_03.text = row[4]
        ball_04 = SubElement(concourse, "ball", {identifier:"4"})
        ball_04.text = row[5]
        ball_05 = SubElement(concourse, "ball", {identifier:"5"})
        ball_05.text = row[6]
        ball_06 = SubElement(concourse, "ball", {identifier:"6"})
        ball_06.text = row[7]
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[8].replace(".", "").replace(",", ".")
        
        hits_6 = SubElement(concourse, "hits_6")
        hits_6_winners = SubElement(hits_6, "winners")
        hits_6_winners.text = row[9]
        hits_6_average = SubElement(hits_6, "average")
        hits_6_average.text = row[10].replace(".", "").replace(",", ".")
        
        hits_5 = SubElement(concourse, "hits_5")
        hits_5_winners = SubElement(hits_5, "winners")
        hits_5_winners.text = row[11]
        hits_5_average = SubElement(hits_5, "average")
        hits_5_average.text = row[12].replace(".", "").replace(",", ".")
        
        hits_4 = SubElement(concourse, "hits_4")
        hits_4_winners = SubElement(hits_4, "winners")
        hits_4_winners.text = row[13]
        hits_4_average = SubElement(hits_4, "average")
        hits_4_average.text = row[14].replace(".", "").replace(",", ".")
        
        accumulated = SubElement(concourse, "accumulated")
        if row[15] == "SIM":
            accumulated.text = "True"
        else:
            accumulated.text = "False"
        
        earned_value = SubElement(concourse, "earned_value")
        earned_value.text = row[16].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[17].replace(".", "").replace(",", ".")
        
        earned_christmas = SubElement(concourse, "earned_cristmas")
        earned_christmas.text = row[18].replace(".", "").replace(",", ".")
        
        return concourse
    
    def lotofacil(self, root, identifier, row):
        """Process each LotoFacil's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
        
        ball_01 = SubElement(concourse, "ball", {identifier:"1"})
        ball_01.text = row[2]
        ball_02 = SubElement(concourse, "ball", {identifier:"2"})
        ball_02.text = row[3]
        ball_03 = SubElement(concourse, "ball", {identifier:"3"})
        ball_03.text = row[4]
        ball_04 = SubElement(concourse, "ball", {identifier:"4"})
        ball_04.text = row[5]
        ball_05 = SubElement(concourse, "ball", {identifier:"5"})
        ball_05.text = row[6]
        ball_06 = SubElement(concourse, "ball", {identifier:"6"})
        ball_06.text = row[7]
        ball_07 = SubElement(concourse, "ball", {identifier:"7"})
        ball_07.text = row[8]
        ball_08 = SubElement(concourse, "ball", {identifier:"8"})
        ball_08.text = row[9]
        ball_09 = SubElement(concourse, "ball", {identifier:"9"})
        ball_09.text = row[10]
        ball_10 = SubElement(concourse, "ball", {identifier:"10"})
        ball_10.text = row[11]
        ball_11 = SubElement(concourse, "ball", {identifier:"11"})
        ball_11.text = row[12]
        ball_12 = SubElement(concourse, "ball", {identifier:"12"})
        ball_12.text = row[13]
        ball_13 = SubElement(concourse, "ball", {identifier:"13"})
        ball_13.text = row[14]
        ball_14 = SubElement(concourse, "ball", {identifier:"14"})
        ball_14.text = row[15]
        ball_15 = SubElement(concourse, "ball", {identifier:"15"})
        ball_15.text = row[16]
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[17].replace(".", "").replace(",", ".")
        
        hits_15 = SubElement(concourse, "hits_15")
        hits_15_winners = SubElement(hits_15, "winners")
        hits_15_winners.text = row[18]
        hits_15_average = SubElement(hits_15, "average")
        hits_15_average.text = row[23].replace(".", "").replace(",", ".")
        
        hits_14 = SubElement(concourse, "hits_14")
        hits_14_winners = SubElement(hits_14, "winners")
        hits_14_winners.text = row[19]
        hits_14_average = SubElement(hits_14, "average")
        hits_14_average.text = row[24].replace(".", "").replace(",", ".")
        
        hits_13 = SubElement(concourse, "hits_13")
        hits_13_winners = SubElement(hits_13, "winners")
        hits_13_winners.text = row[20]
        hits_13_average = SubElement(hits_13, "average")
        hits_13_average.text = row[25].replace(".", "").replace(",", ".")
        
        hits_12 = SubElement(concourse, "hits_12")
        hits_12_winners = SubElement(hits_12, "winners")
        hits_12_winners.text = row[21]
        hits_12_average = SubElement(hits_12, "average")
        hits_12_average.text = row[26].replace(".", "").replace(",", ".")
        
        hits_11 = SubElement(concourse, "hits_11")
        hits_11_winners = SubElement(hits_11, "winners")
        hits_11_winners.text = row[22]
        hits_11_average = SubElement(hits_11, "average")
        hits_11_average.text = row[27].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "accumulated_hits_15")
        estimated_prize.text = row[28].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[29].replace(".", "").replace(",", ".")
        
        return concourse
        
    def quina(self, root, identifier, row):
        """Process each Quina's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
       
        ball_01 = SubElement(concourse, "ball", {identifier:"1"})
        ball_01.text = row[2]
        ball_02 = SubElement(concourse, "ball", {identifier:"2"})
        ball_02.text = row[3]
        ball_03 = SubElement(concourse, "ball", {identifier:"3"})
        ball_03.text = row[4]
        ball_04 = SubElement(concourse, "ball", {identifier:"4"})
        ball_04.text = row[5]
        ball_05 = SubElement(concourse, "ball", {identifier:"5"})
        ball_05.text = row[6]
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[7].replace(".", "").replace(",", ".")
        
        hits_5 = SubElement(concourse, "hits_5")
        hits_5_winners = SubElement(hits_5, "winners")
        hits_5_winners.text = row[8]
        hits_5_average = SubElement(hits_5, "average")
        hits_5_average.text = row[9].replace(".", "").replace(",", ".")
        
        hits_4 = SubElement(concourse, "hits_4")
        hits_4_winners = SubElement(hits_4, "winners")
        hits_4_winners.text = row[10]
        hits_4_average = SubElement(hits_4, "average")
        hits_4_average.text = row[11].replace(".", "").replace(",", ".")
        
        hits_3 = SubElement(concourse, "hits_3")
        hits_3_winners = SubElement(hits_3, "winners")
        hits_3_winners.text = row[12]
        hits_3_average = SubElement(hits_3, "average")
        hits_3_average.text = row[13].replace(".", "").replace(",", ".")
        
        accumulated = SubElement(concourse, "accumulated")
        if row[14] == "SIM":
            accumulated.text = "True"
        else:
            accumulated.text = "False"
        
        earned_value = SubElement(concourse, "earned_value")
        earned_value.text = row[15].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[16].replace(".", "").replace(",", ".")
        
        return concourse
    
    def lotomania(self, root, identifier, row):
        """Process each LotoMania's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
        
        ball_01 = SubElement(concourse, "ball", {identifier:"1"})
        ball_01.text = row[2]
        ball_02 = SubElement(concourse, "ball", {identifier:"2"})
        ball_02.text = row[3]
        ball_03 = SubElement(concourse, "ball", {identifier:"3"})
        ball_03.text = row[4]
        ball_04 = SubElement(concourse, "ball", {identifier:"4"})
        ball_04.text = row[5]
        ball_05 = SubElement(concourse, "ball", {identifier:"5"})
        ball_05.text = row[6]
        ball_06 = SubElement(concourse, "ball", {identifier:"6"})
        ball_06.text = row[7]
        ball_07 = SubElement(concourse, "ball", {identifier:"7"})
        ball_07.text = row[8]
        ball_08 = SubElement(concourse, "ball", {identifier:"8"})
        ball_08.text = row[9]
        ball_09 = SubElement(concourse, "ball", {identifier:"9"})
        ball_09.text = row[10]
        ball_10 = SubElement(concourse, "ball", {identifier:"10"})
        ball_10.text = row[11]
        ball_11 = SubElement(concourse, "ball", {identifier:"11"})
        ball_11.text = row[12]
        ball_12 = SubElement(concourse, "ball", {identifier:"12"})
        ball_12.text = row[13]
        ball_13 = SubElement(concourse, "ball", {identifier:"13"})
        ball_13.text = row[14]
        ball_14 = SubElement(concourse, "ball", {identifier:"14"})
        ball_14.text = row[15]
        ball_15 = SubElement(concourse, "ball", {identifier:"15"})
        ball_15.text = row[16]
        ball_16 = SubElement(concourse, "ball", {identifier:"16"})
        ball_16.text = row[17]
        ball_17 = SubElement(concourse, "ball", {identifier:"17"})
        ball_17.text = row[18]
        ball_18 = SubElement(concourse, "ball", {identifier:"18"})
        ball_18.text = row[19]
        ball_19 = SubElement(concourse, "ball", {identifier:"19"})
        ball_19.text = row[20]
        ball_20 = SubElement(concourse, "ball", {identifier:"20"})
        ball_20.text = row[21]
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[22].replace(".", "").replace(",", ".")
        
        hits_20 = SubElement(concourse, "hits_20")
        hits_20_winners = SubElement(hits_20, "winners")
        hits_20_winners.text = row[23]
        hits_20_average = SubElement(hits_20, "average")
        hits_20_average.text = row[29].replace(".", "").replace(",", ".")
        hits_20_accumulated = SubElement(hits_20, "accumulated")
        hits_20_accumulated.text = row[35].replace(".", "").replace(",", ".")
        
        hits_19 = SubElement(concourse, "hits_19")
        hits_19_winners = SubElement(hits_19, "winners")
        hits_19_winners.text = row[24]
        hits_19_average = SubElement(hits_19, "average")
        hits_19_average.text = row[30].replace(".", "").replace(",", ".")
        hits_19_accumulated = SubElement(hits_19, "accumulated")
        hits_19_accumulated.text = row[36].replace(".", "").replace(",", ".")
        
        hits_18 = SubElement(concourse, "hits_18")
        hits_18_winners = SubElement(hits_18, "winners")
        hits_18_winners.text = row[25]
        hits_18_average = SubElement(hits_18, "average")
        hits_18_average.text = row[31].replace(".", "").replace(",", ".")
        hits_18_accumulated = SubElement(hits_18, "accumulated")
        hits_18_accumulated.text = row[37].replace(".", "").replace(",", ".")
        
        hits_17 = SubElement(concourse, "hits_17")
        hits_17_winners = SubElement(hits_17, "winners")
        hits_17_winners.text = row[26]
        hits_17_average = SubElement(hits_17, "average")
        hits_17_average.text = row[32].replace(".", "").replace(",", ".")
        hits_17_accumulated = SubElement(hits_17, "accumulated")
        hits_17_accumulated.text = row[38].replace(".", "").replace(",", ".")
        
        hits_16 = SubElement(concourse, "hits_16")
        hits_16_winners = SubElement(hits_16, "winners")
        hits_16_winners.text = row[27]
        hits_16_average = SubElement(hits_16, "average")
        hits_16_average.text = row[33].replace(".", "").replace(",", ".")
        hits_16_accumulated = SubElement(hits_16, "accumulated")
        hits_16_accumulated.text = row[39].replace(".", "").replace(",", ".")
        
        hits_0 = SubElement(concourse, "hits_0")
        hits_0_winners = SubElement(hits_0, "winners")
        hits_0_winners.text = row[28]
        hits_0_average = SubElement(hits_0, "average")
        hits_0_average.text = row[34].replace(".", "").replace(",", ".")
        hits_0_accumulated = SubElement(hits_0, "accumulated")
        hits_0_accumulated.text = row[40].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[41].replace(".", "").replace(",", ".")
        
        return concourse
    
    def duplasena(self, root, identifier, row):
        """Process each DuplaSena's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
       
        raffle_1 = SubElement(concourse, "raffle_1")
        
        raffle_1_ball_01 = SubElement(raffle_1, "ball", {identifier:"1"})
        raffle_1_ball_01.text = row[2]
        raffle_1_ball_02 = SubElement(raffle_1, "ball", {identifier:"2"})
        raffle_1_ball_02.text = row[3]
        raffle_1_ball_03 = SubElement(raffle_1, "ball", {identifier:"3"})
        raffle_1_ball_03.text = row[4]
        raffle_1_ball_04 = SubElement(raffle_1, "ball", {identifier:"4"})
        raffle_1_ball_04.text = row[5]
        raffle_1_ball_05 = SubElement(raffle_1, "ball", {identifier:"5"})
        raffle_1_ball_05.text = row[6]
        raffle_1_ball_06 = SubElement(raffle_1, "ball", {identifier:"6"})
        raffle_1_ball_06.text = row[7]
        
        raffle_1_hits_6 = SubElement(raffle_1, "hits_6")
        raffle_1_hits_6_winners = SubElement(raffle_1_hits_6, "raffle_1_hits_6_winners")
        raffle_1_hits_6_winners.text = row[9]
        raffle_1_hits_6_average = SubElement(raffle_1_hits_6, "raffle_1_hits_6_average")
        raffle_1_hits_6_average.text = row[10].replace(".", "").replace(",", ".")
        raffle_1_hits_6_accumulated = SubElement(raffle_1_hits_6, "raffle_1_hits_6_accumulated")
        if row[11] == "SIM":
            raffle_1_hits_6_accumulated.text = "True"
        else:
            raffle_1_hits_6_accumulated.text = "False"
        raffle_1_hits_6_earned_value = SubElement(raffle_1_hits_6, "raffle_1_hits_6_earned_value")
        raffle_1_hits_6_earned_value.text = row[12].replace(".", "").replace(",", ".")
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[8].replace(".", "").replace(",", ".")
        
        raffle_2 = SubElement(concourse, "raffle_2")
        
        raffle_2_ball_01 = SubElement(raffle_2, "ball", {identifier:"1"})
        raffle_2_ball_01.text = row[13]
        raffle_2_ball_02 = SubElement(raffle_2, "ball", {identifier:"2"})
        raffle_2_ball_02.text = row[14]
        raffle_2_ball_03 = SubElement(raffle_2, "ball", {identifier:"3"})
        raffle_2_ball_03.text = row[15]
        raffle_2_ball_04 = SubElement(raffle_2, "ball", {identifier:"4"})
        raffle_2_ball_04.text = row[16]
        raffle_2_ball_05 = SubElement(raffle_2, "ball", {identifier:"5"})
        raffle_2_ball_05.text = row[17]
        raffle_2_ball_06 = SubElement(raffle_2, "ball", {identifier:"6"})
        raffle_2_ball_06.text = row[18]
        
        raffle_2_hits_6 = SubElement(raffle_2, "hits_6")
        raffle_2_hits_6_winners = SubElement(raffle_2_hits_6, "raffle_2_hits_6_winners")
        raffle_2_hits_6_winners.text = row[19]
        raffle_2_hits_6_average = SubElement(raffle_2_hits_6, "raffle_2_hits_6_average")
        raffle_2_hits_6_average.text = row[20].replace(".", "").replace(",", ".")
        raffle_2_hits_5 = SubElement(raffle_2, "hits_5")
        raffle_2_hits_5_winners = SubElement(raffle_2_hits_5, "raffle_2_hits_5_winners")
        raffle_2_hits_5_winners.text = row[21]
        raffle_2_hits_5_average = SubElement(raffle_2_hits_5, "raffle_2_hits_5_average")
        raffle_2_hits_5_average.text = row[22].replace(".", "").replace(",", ".")
        raffle_2_hits_4 = SubElement(raffle_2, "hits_4")
        raffle_2_hits_4_winners = SubElement(raffle_2_hits_4, "raffle_2_hits_4_winners")
        raffle_2_hits_4_winners.text = row[23]
        raffle_2_hits_4_average = SubElement(raffle_2_hits_4, "raffle_2_hits_4_average")
        raffle_2_hits_4_average.text = row[24].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[25].replace(".", "").replace(",", ".")
        
        return concourse
        
    def federal(self, root, identifier, row):
        """Process each Federal's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
       
        prize_01 = SubElement(concourse, "prize", {identifier:"1"})
        prize_01_number = SubElement(prize_01, "number")
        prize_01_number.text = row[2]
        prize_01_value = SubElement(prize_01, "value")
        prize_01_value.text = row[7].replace(".", "").replace(",", ".")
        prize_02 = SubElement(concourse, "prize", {identifier:"2"})
        prize_02_number = SubElement(prize_02, "number")
        prize_02_number.text = row[3]
        prize_02_value = SubElement(prize_02, "value")
        prize_02_value.text = row[8].replace(".", "").replace(",", ".")
        prize_03 = SubElement(concourse, "prize", {identifier:"3"})
        prize_03_number = SubElement(prize_03, "number")
        prize_03_number.text = row[4]
        prize_03_value = SubElement(prize_03, "value")
        prize_03_value.text = row[9].replace(".", "").replace(",", ".")
        prize_04 = SubElement(concourse, "prize", {identifier:"4"})
        prize_04_number = SubElement(prize_04, "number")
        prize_04_number.text = row[5]
        prize_04_value = SubElement(prize_04, "value")
        prize_04_value.text = row[10].replace(".", "").replace(",", ".")
        prize_05 = SubElement(concourse, "prize", {identifier:"5"})
        prize_05_number = SubElement(prize_05, "number")
        prize_05_number.text = row[6]
        prize_05_value = SubElement(prize_05, "value")
        prize_05_value.text = row[11].replace(".", "").replace(",", ".")
        
        return concourse
    
    def lotogol(self, root, identifier, row):
        """Process each LotoGol's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
        
        hits_5 = SubElement(concourse, "hits_5")
        hits_5_winners = SubElement(hits_5, "winners")
        hits_5_winners.text = row[2]
        hits_5_average = SubElement(hits_5, "average")
        hits_5_average.text = row[3].replace(".", "").replace(",", ".")
        hits_5_accumulated = SubElement(hits_5, "accumulated")
        if row[4] == "SIM":
            hits_5_accumulated.text = "True"
        else:
            hits_5_accumulated.text = "False"
        hits_5_earned_value = SubElement(hits_5, "earned_value")
        hits_5_earned_value.text = row[5].replace(".", "").replace(",", ".")
        
        hits_4 = SubElement(concourse, "hits_4")
        hits_4_winners = SubElement(hits_4, "winners")
        hits_4_winners.text = row[6]
        hits_4_average = SubElement(hits_4, "average")
        hits_4_average.text = row[7].replace(".", "").replace(",", ".")
        hits_4_accumulated = SubElement(hits_4, "accumulated")
        if row[8] == "SIM":
            hits_4_accumulated.text = "True"
        else:
            hits_4_accumulated.text = "False"
        hits_4_earned_value = SubElement(hits_4, "earned_value")
        hits_4_earned_value.text = row[9].replace(".", "").replace(",", ".")
        
        hits_3 = SubElement(concourse, "hits_3")
        hits_3_winners = SubElement(hits_3, "winners")
        hits_3_winners.text = row[10]
        hits_3_average = SubElement(hits_3, "average")
        hits_3_average.text = row[11].replace(".", "").replace(",", ".")
        hits_3_accumulated = SubElement(hits_3, "accumulated")
        if row[12] == "SIM":
            hits_3_accumulated.text = "True"
        else:
            hits_3_accumulated.text = "False"
        hits_3_earned_value = SubElement(hits_3, "earned_value")
        hits_3_earned_value.text = row[13].replace(".", "").replace(",", ".")
        
        score_1 = SubElement(concourse, "score", {identifier:"1"})
        score_1_team_1 = SubElement(score_1, "team_1")
        score_1_team_1.text = row[14]
        score_1_team_2 = SubElement(score_1, "team_2")
        score_1_team_2.text = row[15]
        
        score_2 = SubElement(concourse, "score", {identifier:"2"})
        score_2_team_1 = SubElement(score_2, "team_1")
        score_2_team_1.text = row[16]
        score_2_team_2 = SubElement(score_2, "team_2")
        score_2_team_2.text = row[17]
        
        score_3 = SubElement(concourse, "score", {identifier:"3"})
        score_3_team_1 = SubElement(score_3, "team_1")
        score_3_team_1.text = row[18]
        score_3_team_2 = SubElement(score_3, "team_2")
        score_3_team_2.text = row[19]
        
        score_4 = SubElement(concourse, "score", {identifier:"4"})
        score_4_team_1 = SubElement(score_4, "team_1")
        score_4_team_1.text = row[20]
        score_4_team_2 = SubElement(score_4, "team_2")
        score_4_team_2.text = row[21]
        
        score_5 = SubElement(concourse, "score", {identifier:"5"})
        score_5_team_1 = SubElement(score_5, "team_1")
        score_5_team_1.text = row[22]
        score_5_team_2 = SubElement(score_5, "team_2")
        score_5_team_2.text = row[23]
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[24].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[25].replace(".", "").replace(",", ".")
        
        return concourse
        
    def loteca(self, root, identifier, row):
        """Process each Loteca's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
        
        hits_14 = SubElement(concourse, "hits_14")
        hits_14_winners = SubElement(hits_14, "winners")
        hits_14_winners.text = row[2]
        hits_14_average = SubElement(hits_14, "average")
        hits_14_average.text = row[3].replace(".", "").replace(",", ".")
        
        hits_13 = SubElement(concourse, "hits_13")
        hits_13_winners = SubElement(hits_13, "winners")
        hits_13_winners.text = row[6]
        hits_13_average = SubElement(hits_13, "average")
        hits_13_average.text = row[7].replace(".", "").replace(",", ".")
        
        hits_12 = SubElement(concourse, "hits_12")
        hits_12_winners = SubElement(hits_12, "winners")
        hits_12_winners.text = row[8]
        hits_12_average = SubElement(hits_12, "average")
        hits_12_average.text = row[9].replace(".", "").replace(",", ".")
        
        accumulated = SubElement(concourse, "accumulated")
        if row[4] == "SIM":
            accumulated.text = "True"
        else:
            accumulated.text = "False"
        
        earned_value = SubElement(concourse, "earned_value")
        earned_value.text = row[5].replace(".", "").replace(",", ".")
        
        game_01 = SubElement(concourse, "game", {identifier:"1"})
        game_01.text = row[10]
        game_02 = SubElement(concourse, "game", {identifier:"2"})
        game_02.text = row[11]
        game_03 = SubElement(concourse, "game", {identifier:"3"})
        game_03.text = row[12]
        game_04 = SubElement(concourse, "game", {identifier:"4"})
        game_04.text = row[13]
        game_05 = SubElement(concourse, "game", {identifier:"5"})
        game_05.text = row[14]
        game_06 = SubElement(concourse, "game", {identifier:"6"})
        game_06.text = row[15]
        game_07 = SubElement(concourse, "game", {identifier:"7"})
        game_07.text = row[16]
        game_08 = SubElement(concourse, "game", {identifier:"8"})
        game_08.text = row[17]
        game_09 = SubElement(concourse, "game", {identifier:"9"})
        game_09.text = row[18]
        game_10 = SubElement(concourse, "game", {identifier:"10"})
        game_10.text = row[19]
        game_11 = SubElement(concourse, "game", {identifier:"11"})
        game_11.text = row[20]
        game_12 = SubElement(concourse, "game", {identifier:"12"})
        game_12.text = row[21]
        game_13 = SubElement(concourse, "game", {identifier:"13"})
        game_13.text = row[22]
        game_14 = SubElement(concourse, "game", {identifier:"14"})
        game_14.text = row[23]
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[24].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[25].replace(".", "").replace(",", ".")
        
        return concourse
    
    def timemania(self, root, identifier, row):
        """Process each TimeMania's concourse."""
        
        concourse = SubElement(root, "concourse", {identifier:row[0]})
        
        draw_date = SubElement(concourse, "draw_date")
        date = row[1].split("/")
        draw_date.text = "{0}-{1}-{2}".format(date[2], date[1], date[0])
       
        ball_01 = SubElement(concourse, "ball", {identifier:"1"})
        ball_01.text = row[2]
        ball_02 = SubElement(concourse, "ball", {identifier:"2"})
        ball_02.text = row[3]
        ball_03 = SubElement(concourse, "ball", {identifier:"3"})
        ball_03.text = row[4]
        ball_04 = SubElement(concourse, "ball", {identifier:"4"})
        ball_04.text = row[5]
        ball_05 = SubElement(concourse, "ball", {identifier:"5"})
        ball_05.text = row[6]
        ball_06 = SubElement(concourse, "ball", {identifier:"6"})
        ball_06.text = row[7]
        ball_07 = SubElement(concourse, "ball", {identifier:"7"})
        ball_07.text = row[8]
        
        team_heart = SubElement(concourse, "team_heart")
        team_heart.text = row[9]
        
        total_collection = SubElement(concourse, "total_collection")
        total_collection.text = row[10].replace(".", "").replace(",", ".")
        
        hits_7 = SubElement(concourse, "hits_7")
        hits_7_winners = SubElement(hits_7, "winners")
        hits_7_winners.text = row[11]
        hits_7_average = SubElement(hits_7, "average")
        hits_7_average.text = row[17].replace(".", "").replace(",", ".")
        
        hits_6 = SubElement(concourse, "hits_6")
        hits_6_winners = SubElement(hits_6, "winners")
        hits_6_winners.text = row[12]
        hits_6_average = SubElement(hits_6, "average")
        hits_6_average.text = row[18].replace(".", "").replace(",", ".")
        
        hits_5 = SubElement(concourse, "hits_5")
        hits_5_winners = SubElement(hits_5, "winners")
        hits_5_winners.text = row[13]
        hits_5_average = SubElement(hits_5, "average")
        hits_5_average.text = row[19].replace(".", "").replace(",", ".")
        
        hits_4 = SubElement(concourse, "hits_4")
        hits_4_winners = SubElement(hits_4, "winners")
        hits_4_winners.text = row[14]
        hits_4_average = SubElement(hits_4, "average")
        hits_4_average.text = row[20].replace(".", "").replace(",", ".")
        
        hits_3 = SubElement(concourse, "hits_3")
        hits_3_winners = SubElement(hits_3, "winners")
        hits_3_winners.text = row[15]
        hits_3_average = SubElement(hits_3, "average")
        hits_3_average.text = row[21].replace(".", "").replace(",", ".")
        
        hits_team_heart = SubElement(concourse, "hits_team_heart")
        hits_team_heart_winners = SubElement(hits_team_heart, "winners")
        hits_team_heart_winners.text = row[16]
        hits_team_heart_average = SubElement(hits_team_heart, "average")
        hits_team_heart_average.text = row[22].replace(".", "").replace(",", 
            ".")
        
        earned_value = SubElement(concourse, "earned_value")
        earned_value.text = row[23].replace(".", "").replace(",", ".")
        
        estimated_prize = SubElement(concourse, "estimated_prize")
        estimated_prize.text = row[24].replace(".", "").replace(",", ".")
        
        return concourse

#EOF
