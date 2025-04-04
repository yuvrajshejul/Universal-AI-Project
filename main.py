\chapter{SOFTWARE DESIGN}
\textbf{Block diagram and its explanation:}
\item \textbf{7.1 User:}
\item Implements user-related actions, including Register() method for user registration and incorporating Login() method for user authentication.

\item \textbf{7.2 Dashboard :}
\item Central hub with various features, containing HealthcareSchemes() for navigating to healthcare schemes, providing BookAppointment() for doctor appointment booking, including TapToChat() for chatbot interactions, and featuring TapToAsk() for asking questions using voice commands.

\item \textbf{7.3 HealthcareSchemes  :}
\item Manages the display of disease categories and government schemes, including viewDiseaseCategories() method for showing available disease categories and incorporating viewGovernmentSchemes() method for displaying government healthcare schemes.

\item \textbf{7.4 DiseaseCategory  :}
\item Represents specific disease categories and includes viewSchemes() method for displaying government schemes related to the selected disease category.

\item \textbf{7.5 BookAppointment  :}
\item Manages doctor appointment booking with methods for choosing a doctor, selecting date and time, and confirming the appointment.

\item \textbf{7.6 TapToChat :}
\item Enables chat interactions with the chatbot, featuring chatWithChatbot() and getHomeRemedies() methods.

\item \textbf{7.7 TapToAsk :}
\item Enables voice-based question interaction with askWithVoice() method and provides home remedies information through getHomeRemedies() method.

\item \textbf{7.8 PMJAY :}
\item Represents the Pradhan Mantri Jan Arogya Yojana (PMJAY) government healthcare scheme, featuring getDetails() method for retrieving scheme details.

\item \textbf{7.9 AyushmanBharat :}
\item Represents the Ayushman Bharat government healthcare scheme, featuring getDetails() method for retrieving scheme details.

\item \textbf{7.10 HomeRemedies :}
\item Provides home remedies information, including displayRemedies() method for showing remedies in both chat and voice interactions.
