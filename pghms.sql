-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 01, 2024 at 02:35 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pghms`
--

-- --------------------------------------------------------

--
-- Table structure for table `hostels`
--

CREATE TABLE `hostels` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `lat` float NOT NULL,
  `lon` float NOT NULL,
  `location` varchar(200) NOT NULL,
  `image_url` varchar(500) NOT NULL,
  `map_embed_url` varchar(500) NOT NULL,
  `avg_rating` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hostels`
--

INSERT INTO `hostels` (`id`, `name`, `lat`, `lon`, `location`, `image_url`, `map_embed_url`, `avg_rating`) VALUES
(1, 'Zostel Bangalore (Indiranagar)', 12.9651, 77.642, '2032, 17th Main, 1st Cross Rd, HAL 2nd Stage, Indiranagar, Bengaluru, Karnataka 560038', 'https://lh5.googleusercontent.com/p/AF1QipMNi0Ys_gIEvPyWY_xAFOAh-lJxpmsHBOrOM4QX=w253-h189-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.1094182499087!2d77.63946937484125!3d12.964849687349892!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1521862d28c7%3A0x9479d42b47fb6289!2sZostel%20Bangalore%20(Indiranagar)!5e0!3m2!1sen!2sin!4v1718893491441!5m2!1sen!2sin', 4.56),
(2, 'The Hosteller Bangalore, Indiranagar', 12.9725, 77.645, '68, 1st Main Rd, Hal, HAL 3rd Stage, New Tippasandra, Indiranagar, Bengaluru, Karnataka 560075', 'https://lh3.googleusercontent.com/p/AF1QipMs2Sc66TEpcYEmiZWKG9IeN6CnP2oazHc5rd2n=w287-h192-n-k-rw-no-v1', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.98963828953!2d77.64496997484132!3d12.972514387342972!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae116ca8259d95%3A0x9059d3ef46b4027c!2sThe%20Hosteller%20Bangalore%2C%20Indiranagar!5e0!3m2!1sen!2sin!4v1718896098765!5m2!1sen!2sin', 4.72),
(3, 'WOKE - Indiranagar, Bangalore', 12.9779, 77.6418, '715, 2nd Cross Rd, behind Max Muller Bhavan, Indira Nagar 1st Stage, Defence Colony, Indiranagar, Bengaluru, Karnataka 560038', 'https://lh3.googleusercontent.com/p/AF1QipOcFbLPkbhyuNIzB3jJeEZUCGtBWjUEOHtUdxJO=w287-h192-n-k-rw-no-v1', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.9059087095334!2d77.64177827484146!3d12.977869587338112!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae17186f7483a1%3A0x71bf0d1564e70007!2sWOKE%20-%20Indiranagar%2C%20Bangalore!5e0!3m2!1sen!2sin!4v1718902035724!5m2!1sen!2sin', 4.1),
(4, 'Poorna Bodha PG', 12.9983, 77.5535, '1760, Mahakavi Kuvempu Rd, Mariappanapalya, Rajajinagar, Bengaluru, Karnataka 560021', 'https://lh5.googleusercontent.com/p/AF1QipMzfwu729d1f7AxzlFd1aWkkzYPikdmFiu71PFf=w408-h725-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15550.713283765534!2d77.54627789528362!3d12.99241474719566!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d8f76a47449%3A0xa9a1c4e3b59b98be!2sPOORNA%20BODHA%20PG!5e0!3m2!1sen!2sin!4v1718942737575!5m2!1sen!2sin', 4.67),
(5, 'Balaji Hostels for Women & Paying Guest', 12.9998, 77.5521, '24, 12th Main Rd, 1st Block, Rajajinagar, Bengaluru, Karnataka 560010', 'https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=GLNfea6rImS7_LeAlGq4xg&cb_client=search.gws-prod.gps&w=408&h=240&yaw=63.394333&pitch=0&thumbfov=100', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15550.68059129598!2d77.53173698321007!3d12.992936794376291!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d8f8e53f887%3A0x5ffbbfffd391d130!2sBalaji%20hostels%20for%20women%20%26%20Paying%20Guest!5e0!3m2!1sen!2sin!4v1718943261500!5m2!1sen!2sin', 3.8),
(6, 'Sri Adichunchanagiri Free Hostel For Girls', 13.0052, 77.5456, '#CA 6 & 7, 2nd Block, West of Chord Road 2nd Stage, West of Chord Road, Stage 2, Mahalakshmi Layout, Bengaluru, Karnataka 560086', 'NULL', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15550.680616698095!2d77.53173697926195!3d12.992936388752582!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d9c0fe15c61%3A0xdf9a3a30e9fa1ef3!2sSri%20Adichunchanagiri%20Free%20Hostel%20For%20Girls!5e0!3m2!1sen!2sin!4v1718943411146!5m2!1sen!2sin', 4),
(7, 'Sai Shardhamba Ladies PG', 12.987, 77.5146, 'Basaveshwar Nagar,Bengaluru', 'https://lh5.googleusercontent.com/p/AF1QipML51AVgkYIfG1PkibSwSPh2okRjaffEgn-B6Ux=w427-h240-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15551.050182772775!2d77.5146201871582!3d12.9870338!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3dbf56826525%3A0xd4ae6563e2f8ed4c!2sSai%20Shardhamba%20ladies%20PG!5e0!3m2!1sen!2sin!4v1718943611701!5m2!1sen!2sin', 4.44),
(8, 'Zolo Paradise - PG in Sanjay nagar', 13.0292, 77.5758, '6th Cross Rd, Banday Colony, Geddalahalii, Sanjay Nagar, Bengaluru, Karnataka 560094', 'https://lh5.googleusercontent.com/p/AF1QipPapUxGMUIA3nnfLrgFz7owwTAhyKJfhExGE-zK=w408-h306-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.106430602048!2d77.57316887484242!3d13.028893887291696!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae17b80ad30deb%3A0x19810c950a7a78e1!2sZolo%20Paradise%20-%20PG%20in%20Sanjay%20nagar!5e0!3m2!1sen!2sin!4v1719550295446!5m2!1sen!2sin', 4.65),
(9, 'Sri Sai Luxurious Guest House', 13.0364, 77.5747, '5, 2nd Main Road, 3rd Cross Rd, Naidu Layout, Sanjay Nagar, Bengaluru, Karnataka 560094', 'https://lh5.googleusercontent.com/p/AF1QipPhC2JoCJPX1e26UT38PhyewpVhdRMOC6z-ZkCd=w408-h306-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3886.9747208810636!2d77.57256067484253!3d13.037281037284163!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae17e85d895b57%3A0x7542c59dab46914b!2sSri%20Sai%20Luxurious%20Guest%20House!5e0!3m2!1sen!2sin!4v1719739661962!5m2!1sen!2sin', 4.61),
(10, 'Guru Sri gents pg', 12.933, 77.5694, '15th cross road, 6th Main Rd, Banashankari 2nd Stage, Bengaluru, Karnataka 560070', 'https://lh5.googleusercontent.com/p/AF1QipOFv9S58IeRAwyrje5Bxy6nhSrumrRhEndxBez9=w408-h306-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d62218.65630483146!2d77.4945715486328!3d12.92917430000002!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae15f5aafaa9d1%3A0x95dcd69b20687997!2sGuru%20Sri%20gents%20pg!5e0!3m2!1sen!2sin!4v1719550931826!5m2!1sen!2sin', 4.24),
(11, 'Mathru Priya Ladies Hostel', 12.9755, 77.5344, '37/8, Govindaraja Nagar Ward, Gangadhar Layout, Vijayanagar, Bengaluru, Karnataka 560040', 'https://lh5.googleusercontent.com/p/AF1QipNRbmhUXLx0VE_AHFEhSvtP2ZO4d5-XRIyXTC-e=w425-h240-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.945197922307!2d77.53183707484152!3d12.975356987340332!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3dd955555555%3A0x6db535166b3a2caa!2sMathru%20Priya%20Ladies%20Hostel!5e0!3m2!1sen!2sin!4v1719565949484!5m2!1sen!2sin', 3.5),
(12, 'Shri Jagatjyothi Basaveshwara Hostel,Manuvana,vijayanagar', 12.975, 77.5462, 'Govindaraja Nagar Ward, Stage 1, Vijayanagar, Bengaluru, Karnataka 560040', 'https://lh5.googleusercontent.com/p/AF1QipOsQ3S7ewwgkGj3OPrgwopmubKosUBT5BuMPjPB=w408-h725-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.956409837619!2d77.54577552305845!3d12.974639881998758!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3de5bf94fb15%3A0x848782e304d2d8f!2sShri%20Jagatjyothi%20Basaveshwara%20Hostel%2Cmanuvana%2Cvijayanagar!5e0!3m2!1sen!2sin!4v1719566185865!5m2!1sen!2sin', 4.06),
(13, 'Priya Executive PG (for Ladies)', 12.9895, 77.5395, '375, 5th Main Rd, near mathru speciality hospital, 3rd Block, West Of Chord Road, 3rd Stage, Basaveshwar Nagar, Bengaluru, Karnataka 560079', 'https://streetviewpixels-pa.googleapis.com/v1/thumbnail?panoid=epU8oXFXFJlx6JF5KgAfCw&cb_client=search.gws-prod.gps&w=408&h=240&yaw=356.55228&pitch=0&thumbfov=100', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.7269361641293!2d77.53687257484168!3d12.989309087327682!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d1a91e8354b%3A0x4f6d94bf43845ccd!2sPriya%20Executive%20PG%20(for%20Ladies)!5e0!3m2!1sen!2sin!4v1719735860109!5m2!1sen!2sin', 3.61),
(14, 'The Beehive Hostel Luxury mens PG', 12.9241, 77.5716, '2237, 23rd Cross Rd, next to Karnataka Grameena Bank, Karesandra, Banashankari 2nd Stage, Banashankari, Bengaluru, Karnataka 560070', 'https://lh5.googleusercontent.com/p/AF1QipNGh2-lueYewMjs5v4cBDRkEfiZdP-JfqehSwWQ=w507-h240-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.7470617392773!2d77.56910517484053!3d12.923971787387094!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae15831ea54555%3A0xa6a6d60314735122!2sThe%20Beehive%20Hostel%20Luxury%20mens%20PG!5e0!3m2!1sen!2sin!4v1719736051304!5m2!1sen!2sin', 4.49),
(15, 'Kambi Siddaramanna Hostel ಕಂಬಿ ಸಿದ್ದರಾಮಣ್ಣ ವಿದ್ಯಾರ್ಥಿ ನಿಲಯ', 12.9896, 77.5371, '4th Block, 1st A Cross, 3rd Stage, Basaveshwar Nagar, Bengaluru, Karnataka 560079', 'https://lh5.googleusercontent.com/p/AF1QipMcfGgXkDQ9ce3vSVPbfQyhbD1rjKwfz15Q159f=w408-h306-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.72785179889!2d77.53450137484167!3d12.989250587327744!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d96aaaaaaab%3A0x51499aec14bbaecb!2zS2FtYmkgU2lkZGFyYW1hbm5hIEhvc3RlbCDgspXgsoLgsqzgsr8g4LK44LK_4LKm4LON4LKm4LKw4LK-4LKu4LKj4LON4LKjIOCyteCyv-CypuCzjeCyr-CyvuCysOCzjeCypeCyvyDgsqjgsr_gsrLgsq8!5e0!3m2!1sen!2sin!4v1719737582146!5m2!1sen!2sin', 4.28),
(16, 'Padma Ladies PG', 12.9222, 77.5682, '35,30th Cross, 10th Main Rd, near KAVERI nagar, Banashankari 2nd Stage, busstop, Bengaluru, Karnataka 560070', 'https://lh5.googleusercontent.com/p/AF1QipOHorRvEKQk7UXD2xSh82dqBLx5l3g-basdQgX2=w408-h541-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15554.328393286072!2d77.5387139871582!3d12.934559400000026!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae157074cb6427%3A0x80b8efd8efa44ca!2sPadma%20Ladies%20PG!5e0!3m2!1sen!2sin!4v1720280886949!5m2!1sen!2sin\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade', 4.29),
(17, 'Sri Varshini PG For Gents', 12.9936, 77.5509, '390/A, Chord Rd, Manjunath Nagar, Rajajinagar, Bengaluru, Karnataka 560010', 'https://lh5.googleusercontent.com/p/AF1QipN3QPVD6ia_-Cih73zoiPTm2XwHoa__aSzw6flz=w408-h905-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15550.680565893905!2d77.53173698715818!3d12.992937200000013!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d8fd9473325%3A0x4e287675cdb7e5cd!2sSri%20Varshini%20PG%20For%20gents!5e0!3m2!1sen!2sin!4v1718943009420!5m2!1sen!2sin', 4.62),
(18, 'Prakruthi Youth Hostel', 12.926, 77.5739, '493/j, 8th Cross Rd, 7th Block, Jayanagar, Bengaluru, Karnataka 560070', 'https://lh5.googleusercontent.com/p/AF1QipPhOR4YzuyrJyxJ8meY90IGFH8oMERObO0yOMYj=w408-h306-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.7192593271866!2d77.57123517484054!3d12.925756787385446!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae159cb0c2ab07%3A0x134d0cea6a6ce25b!2sPrakruthi%20Youth%20Hostel!5e0!3m2!1sen!2sin!4v1718902218556!5m2!1sen!2sin', 3.1),
(19, 'ECO PG Hostels Jayanagar', 12.93, 77.5872, '13th Main Rd, 4th T Block East, 4th Block, Jayanagar, Bengaluru, Karnataka 560041', 'https://lh5.googleusercontent.com/p/AF1QipP95yZPzTLF8tgiVvXha6TM3GvzrPz-sSQ1rdiO=w408-h409-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.657287645851!2d77.58452927484062!3d12.929734687381798!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1505b5ad1487%3A0xc24511525d3227b!2sECO%20PG%20Hostels%20Jayanagar!5e0!3m2!1sen!2sin!4v1718902363182!5m2!1sen!2sin', 3.8),
(20, 'MEERA PAYING GUEST ACCOMODATION FOR LADIES', 12.9297, 77.5611, 'Excellent Paying Guest Accomodation, Kaveri Nagar, Banagirinagara, Banashankari 3rd Stage, Banashankari, Bengaluru, Karnataka 560085', 'https://lh5.googleusercontent.com/p/AF1QipMjN2ZyKIynsHrK8vfNME__KqxUbZqaw8SB_-rM=w408-h463-k-no\n', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15554.702578296135!2d77.5612513!3d12.9285565!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3fa62873216f%3A0x953ea4f86b8b6bf2!2sMEERA%20PAYING%20GUEST%20ACCOMODATION%20FOR%20LADIES!5e0!3m2!1sen!2sin!4v1720460594511!5m2!1sen!2sin\" width=\"600\" height=\"450\" style=\"border:0;\" allowfullscreen=\"\" loading=\"lazy\" referrerpolicy=\"no-referrer-when-downgrade', 4.3),
(21, 'CMA Boys Hostel', 12.9434, 77.5806, '560082, 18/2, Vedantha Mandir Rd, 2nd Block, Jayanagar East, Jayanagar, Bengaluru, Karnataka 560004', 'https://lh5.googleusercontent.com/p/AF1QipPihviQbPoPi8fV4KU0X28pS8YEiUWErlXnDCha=w426-h240-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d75000.37423469531!2d77.49861656115723!3d13.006688289066265!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae15969a33d3df%3A0xc04e964dc71c5246!2sCMA%20Boys%20Hostel.!5e0!3m2!1sen!2sin!4v1719549430707!5m2!1sen!2sin', 4.6),
(22, 'Zolo Splendour - PG ', 13.0135, 77.5476, '9, 9, Mahalakshmi Layout Main Rd, Yeshwanthpur Industrial Suburb, Mahalakshmi Layout, Bengaluru, Karnataka 560096', 'https://lh5.googleusercontent.com/p/AF1QipNqA7P1V7ESL68EFsw0xhVUwgoWZdq_8tKiN-vR=w408-h271-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.3530072775507!2d77.5450521248421!3d13.013177837306042!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d6b6af16085%3A0x58cab0d5952ff5d4!2sZolo%20Splendour%20-%20PG%20in%20Yeshwanthpur!5e0!3m2!1sen!2sin!4v1719738121143!5m2!1sen!2sin', 4.2),
(23, 'Sri Sai PG Accommodation For Men', 13.0189, 77.5465, '783/C, 2nd Cross Rd, near ORCHIDS INTERNATIONAL SCHOOL, Mahalakshmipuram Layout, Mahalakshmi Layout, Bengaluru, Karnataka 560086', 'https://lh5.googleusercontent.com/p/AF1QipNYxHwECmmLu31nUG8JSf9g8Doyz2PC0RZvQKE=w408-h544-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d124413.02443608233!2d77.47611245289212!3d12.97779893282168!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d27cd93ac29%3A0x83e60fd32383b1df!2sSri%20Sai%20PG%20Accommodation%20For%20Men!5e0!3m2!1sen!2sin!4v1719738322678!5m2!1sen!2sin', 3.13),
(24, 'Zolo Hibiscus ', 12.9261, 77.6148, '45, 6th Cross Rd, Zuzuvadi, Maruti Nagar, 1st Stage, BTM Layout, Bengaluru, Karnataka 560029', 'https://lh5.googleusercontent.com/p/AF1QipMrPyN0scXJsbbpKHutM8uTd2InMg4tZBmYfNBc=w426-h240-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7777.450228031049!2d77.60966243889379!3d12.925380918605512!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae145660455555%3A0x8d5f65fb73e661b7!2sZolo%20Hibiscus%20-%20Best%20PG%20in%20BTM%20Layout%20%7C%20Coliving%20PG!5e0!3m2!1sen!2sin!4v1719738520340!5m2!1sen!2sin', 4.26),
(25, 'Zolo Asha', 12.9196, 77.6162, '152, 8th Cross Rd, Old Madiwala, Jay Bheema Nagar, 1st Stage, BTM Layout, Bengaluru, Karnataka 560029', 'https://lh5.googleusercontent.com/p/AF1QipNpyhV9lqQzhbE2MWfVFUOV2Lf9CWozvUF3W8f3=w408-h272-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.8202784982345!2d77.6136801748404!3d12.919269887391328!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae155992657a0b%3A0x932aea2da00a7316!2sZolo%20Asha%20-%20Best%20PG%20in%20BTM%20Layout%20%7C%20Coliving%20PG!5e0!3m2!1sen!2sin!4v1719738729137!5m2!1sen!2sin', 4.07),
(26, 'The Little Blue Window Hostel', 12.9139, 77.6088, '743, 13th Main Road, Sunshine Colony, Stage 2, 2nd Stage, BTM 2nd Stage, BTM Layout, Bengaluru, Karnataka 560076', 'https://lh5.googleusercontent.com/p/AF1QipMBE0jvrbM9vNgWuDZIHSLJB-w8rVRgN-Q53_As=w408-h306-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.906899827423!2d77.6062510748403!3d12.913704987396343!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae14fd717a4c3b%3A0x7e177e437f0db4c3!2sThe%20Little%20Blue%20Window%20Hostel!5e0!3m2!1sen!2sin!4v1719738838074!5m2!1sen!2sin', 4.38),
(27, 'Zolo Mishal PG in Mathikere | Coliving PG', 13.0302, 77.5784, '33, near Corporation Bank, KEB Layout, Sanjay Nagar, Bengaluru, Karnataka 560094', 'https://lh5.googleusercontent.com/p/AF1QipPPaC4PYXtQZDd7SOrSVqcBKcI8YYFcpv_-hPE=w408-h305-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3887.0888048285237!2d77.57577737484246!3d13.030016587290696!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1755c912127b%3A0xf4b881eb1f586c91!2sZolo%20Mishal%20PG%20in%20Mathikere%20%7C%20Coliving%20PG!5e0!3m2!1sen!2sin!4v1719739119150!5m2!1sen!2sin', 4.4),
(28, 'S.S Boys PG - JP Nagar', 12.9105, 77.573, 'No.185, s.s towers, Bus Stop, Kanakapura Rd, opposite to Sarakki Gate, Umarbagh Layout, J.P. Nagar, Bengaluru, Karnataka 560078', 'https://lh5.googleusercontent.com/p/AF1QipPlCrSA2MZHfxVAPYGPUXStIPLJkhbAerccY8Ml=w408-h612-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7777.932930456159!2d77.56327189357913!3d12.909876900000011!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae154321098501%3A0x160ea46c4584e8a9!2sS.S%20Boys%20PG%20-%20JP%20Nagar!5e0!3m2!1sen!2sin!4v1719739841863!5m2!1sen!2sin', 4.22),
(29, 'Jain Student Hostel', 12.9083, 77.5903, '10/3/C, 17TH MAIN, 15th Cross Rd, 5th Phase, JP Nagar Phase 6, J.P. Nagar, Bengaluru, Karnataka 5600078', 'https://lh5.googleusercontent.com/p/AF1QipOm9sB1OS-VzB3IjORX2J-jvM83bXyX7wrHWAJp=w408-h272-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31109.221235206507!2d77.56133624610369!3d12.930032042397439!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae1513dfba69a1%3A0xbc97d920f6465fab!2sJain%20Student%20Hostel!5e0!3m2!1sen!2sin!4v1719740121392!5m2!1sen!2sin', 3.65),
(30, 'Shirdi sai mansion pg', 12.9128, 77.5923, '9, 16th Main Rd, KSRTC Layout, 2nd Phase, J.P. Nagar, Bengaluru, Karnataka 560078', 'https://lh5.googleusercontent.com/p/AF1QipOrDxqbiX75JCxaUA2MW-QdKNpnfChs0PIh57kD=w427-h240-k-no', 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3888.9238294196643!2d77.58976947484037!3d12.91261708739737!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae152dcd71167b%3A0x5f6efc2d158b89db!2sShirdi%20sai%20mansion%20pg!5e0!3m2!1sen!2sin!4v1719740247192!5m2!1sen!2sin', 4.81);

-- --------------------------------------------------------

--
-- Table structure for table `owner_pgh`
--

CREATE TABLE `owner_pgh` (
  `id` int(11) NOT NULL,
  `Owner_Name` text NOT NULL,
  `Phone_Number` varchar(11) NOT NULL,
  `Email_Id` varchar(30) NOT NULL,
  `Amenities` text NOT NULL,
  `Single Room` int(11) NOT NULL,
  `Double Sharing` int(11) NOT NULL,
  `Triple Sharing` int(11) NOT NULL,
  `Four Sharing` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Name` text NOT NULL,
  `User_Id` varchar(40) NOT NULL,
  `Phone_Number` varchar(12) NOT NULL,
  `Email_Id` varchar(40) NOT NULL,
  `Password` varchar(255) NOT NULL,
  `State` text NOT NULL,
  `District` text NOT NULL,
  `OTP` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Name`, `User_Id`, `Phone_Number`, `Email_Id`, `Password`, `State`, `District`, `OTP`) VALUES
('Vishruth M V', 'vmv@123', '9000800070', 'vishruth.mv10@gmail.com', '$2y$10$LKEYzm61MG8bQ3GdbbLQm.BJUbq3ihJ4bmlN6NmD.Biu.zm6RWpki', 'Karnataka', 'Bengaluru Urban', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hostels`
--
ALTER TABLE `hostels`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `owner_pgh`
--
ALTER TABLE `owner_pgh`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`User_Id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `owner_pgh`
--
ALTER TABLE `owner_pgh`
  ADD CONSTRAINT `owner_pgh_ibfk_1` FOREIGN KEY (`id`) REFERENCES `hostels` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
