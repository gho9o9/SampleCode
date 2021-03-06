USE [master]
GO

/****** Object:  Database [sql17mlhandson]    Script Date: 2017/11/21 21:31:58 ******/
CREATE DATABASE [sql17mlhandson]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'sql17mlhandson', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\sql17mlhandson.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'sql17mlhandson_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL14.MSSQLSERVER\MSSQL\DATA\sql17mlhandson_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
GO

ALTER DATABASE [sql17mlhandson] SET COMPATIBILITY_LEVEL = 140
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [sql17mlhandson].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO

ALTER DATABASE [sql17mlhandson] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [sql17mlhandson] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [sql17mlhandson] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [sql17mlhandson] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [sql17mlhandson] SET ARITHABORT OFF 
GO

ALTER DATABASE [sql17mlhandson] SET AUTO_CLOSE OFF 
GO

ALTER DATABASE [sql17mlhandson] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [sql17mlhandson] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [sql17mlhandson] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [sql17mlhandson] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [sql17mlhandson] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [sql17mlhandson] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [sql17mlhandson] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [sql17mlhandson] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [sql17mlhandson] SET  DISABLE_BROKER 
GO

ALTER DATABASE [sql17mlhandson] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [sql17mlhandson] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [sql17mlhandson] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [sql17mlhandson] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [sql17mlhandson] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [sql17mlhandson] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [sql17mlhandson] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [sql17mlhandson] SET RECOVERY FULL 
GO

ALTER DATABASE [sql17mlhandson] SET  MULTI_USER 
GO

ALTER DATABASE [sql17mlhandson] SET PAGE_VERIFY CHECKSUM  
GO

ALTER DATABASE [sql17mlhandson] SET DB_CHAINING OFF 
GO

ALTER DATABASE [sql17mlhandson] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [sql17mlhandson] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO

ALTER DATABASE [sql17mlhandson] SET DELAYED_DURABILITY = DISABLED 
GO

ALTER DATABASE [sql17mlhandson] SET QUERY_STORE = OFF
GO

USE [sql17mlhandson]
GO

ALTER DATABASE SCOPED CONFIGURATION SET IDENTITY_CACHE = ON;
GO

ALTER DATABASE SCOPED CONFIGURATION SET LEGACY_CARDINALITY_ESTIMATION = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET LEGACY_CARDINALITY_ESTIMATION = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET MAXDOP = 0;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET MAXDOP = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET PARAMETER_SNIFFING = ON;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET PARAMETER_SNIFFING = PRIMARY;
GO

ALTER DATABASE SCOPED CONFIGURATION SET QUERY_OPTIMIZER_HOTFIXES = OFF;
GO

ALTER DATABASE SCOPED CONFIGURATION FOR SECONDARY SET QUERY_OPTIMIZER_HOTFIXES = PRIMARY;
GO

ALTER DATABASE [sql17mlhandson] SET  READ_WRITE 
GO


