import React from 'react'
import * as AiIcons from 'react-icons/ai';
import * as FaIcons from 'react-icons/fa';
import * as IoIcons from 'react-icons/io';

export const SidebarData = [
    {
        title: 'Home',
        path: '/',
        icon: <AiIcons.AiFillHome />,
        cName:'nav-text'
    },
    {
        title: 'Courses',
        path: '/courses',
        icon: <IoIcons.IoIosPaper />,
        cName:'nav-text'
    }, {
        title: 'Certificates',
        path: '/certificates',
        icon: <FaIcons.FaGraduationCap />,
        cName:'nav-text'
    }, 
    {
        title: 'Staff',
        path: '/staff',
        icon: <IoIcons.IoMdPeople />,
        cName:'nav-text'
    },
    {
        title: 'Contact',
        path: '/contact',
        icon: <IoIcons.IoMdCall />,
        cName:'nav-text'
    },
    {
        title: 'Socials',
        path: '/socials',
        icon: <AiIcons.AiFillInstagram />,
        cName:'nav-text'
    },
]
