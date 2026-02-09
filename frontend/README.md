# Todo Frontend Application

This is the frontend for the Todo application built with Next.js, TypeScript, and Tailwind CSS.

## Features

- User authentication (signup/login)
- Todo management (create, read, update, delete, toggle completion)
- Responsive design for desktop and mobile
- Loading and error states
- Protected routes

## Tech Stack

- Next.js 16+
- React 19+
- TypeScript
- Tailwind CSS
- Axios for API requests
- Better Auth for authentication

## Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```

2. Set up environment variables:
   Create a `.env.local` file in the root of the frontend directory with the following:
   ```
   NEXT_PUBLIC_API_BASE_URL=http://localhost:8000/api
   NEXT_PUBLIC_JWT_SECRET=your-jwt-secret-here
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser to see the application.

## Available Scripts

- `npm run dev` - Start the development server
- `npm run build` - Build the application for production
- `npm start` - Start the production server
- `npm run lint` - Run ESLint
- `npm run test` - Run tests
- `npm run format` - Format code with Prettier

## Project Structure

```
frontend/
├── src/
│   ├── app/                 # Next.js App Router pages
│   │   ├── (auth)/         # Authentication routes (login, signup)
│   │   └── dashboard/      # Protected routes for authenticated users
│   ├── components/         # Reusable UI components
│   │   ├── auth/           # Authentication-related components
│   │   ├── todos/          # Todo-specific components
│   │   ├── ui/             # Base UI components
│   │   └── providers/      # Context providers
│   ├── lib/                # Utility functions and shared logic
│   │   ├── auth/           # Authentication utilities
│   │   ├── api/            # API communication layer
│   │   └── utils/          # General utility functions
│   └── types/              # TypeScript type definitions
├── tests/                  # Test files
├── public/                 # Static assets
├── package.json
├── next.config.js
├── tsconfig.json
└── tailwind.config.js
```

## API Endpoints Used

The application communicates with the backend API at the base URL specified in the environment variables. The following endpoints are used:

- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User login
- `GET /api/todos` - Get all todos for the authenticated user
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/{id}` - Update an existing todo
- `DELETE /api/todos/{id}` - Delete a todo
- `PATCH /api/todos/{id}/toggle` - Toggle the completion status of a todo